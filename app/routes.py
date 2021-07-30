from flask import render_template, flash, redirect, url_for, request
from app import app 
from flask_login import current_user, login_user
from app.models import User, Artifact, Handover, Media, Text, MediaType
from app.forms import RegisterForm, UpdateForm
from app import db
@app.route('/')
@app.route('/index')
def index():
	return render_template('/index.html')
@app.route('/login', methods=['GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user_id = request.args.get('user_id')
    access_hash = request.args.get('access_hash')
    user = User.query.get(user_id)
    if user is None or user.access_hash != access_hash:
    	flash('Invalid user id and access hash combination')
    	return redirect(url_for('index'))
    login_user(user)
    return redirect(url_for('index'))
@app.route('/coin/<artifact_id>')
@app.route('/coin/<artifact_id>/<artifact_hash>')
def artifact(artifact_id=0, artifact_hash=False):
	artifact = Artifact.query.get(artifact_id)
	return jsonify(artifact.all())

@app.route('/.well-known/acme-challenge/<challenge>')
def letsencrypt_check(challenge):
    challenge_response = {
        "<challenge_token>":"<challenge_response>",
        "<challenge_token>":"<challenge_response>"
    }
    return Response(challenge_response[challenge], mimetype='text/plain')


@app.route('/register/<artifact_id>/<artifact_hash>', methods=['GET','POST'])
def register(artifact_id, artifact_hash):
	artifact = Artifact.query.get(artifact_id)
	form = RegisterForm(request.form)
	print (request.method)
	if form.is_submitted():
		print ("submitted")
		print (form.email.data)
	if form.validate_on_submit():
		print ("valid")
	else: 
		print(form.errors)
	if artifact_id is None or artifact.access_hash != artifact_hash:
		flash("invalid artifact id and access hash combination")
		return redirect(url_for('index'))
	if request.method == 'POST'and form.validate_on_submit():
		user = User.get_or_create_user(form.email.data, form.name.data)
		predecessor = Handover.query.join(Artifact).filter(Artifact.id==Handover.artifact_id).filter(Artifact.id==artifact.id).order_by(Handover.id.desc()).limit(1).one_or_none()
		if predecessor != None:
			predecessor_id = predecessor.id
		else: 
			predecessor_id = None
		if form.text.data != "":
			media = Media(type=MediaType.text)
			db.session.add(media)
			db.session.commit()
			text = Text(media_id = media.id, text = form.text.data)
			db.session.add(text)
			db.session.commit()
		handover = Handover(artifact_id=artifact_id,predecessor_id = predecessor_id, lat = form.lat.data, lon = form.lon.data, user_id = user.id)
		handover.media_id = media.id
		db.session.add(handover)
		db.session.commit()
		return redirect(url_for('handover', handover_id = handover.id))
	handover_count = Handover.query.join(Artifact).filter(Artifact.id==Handover.artifact_id).count()
	return render_template('register.html',title = "Register Handover", form=form, artifact_id = artifact_id, handover_count = handover_count, access_hash=artifact_hash)
	
@app.route('/handover/<handover_id>/', methods=['GET', 'POST'])
@app.route('/handover/<handover_id>/<handover_hash>', methods=['GET', 'POST'])
def handover(handover_id, handover_hash = None):
	form = UpdateForm()
	handover = Handover.query.get(handover_id)
	user = User.query.get(handover.user_id)
	text = Text.query.join(Media).filter(Media.id == Text.media_id).join(Handover).filter(Media.id == Handover.media_id).filter(Handover.id == handover_id).limit(1)
	handover_count = Handover.query.filter(Handover.artifact_id==handover.artifact_id).count()
	print("text")
	print (text[0].text)
	if handover == None: 
		return redirect(url_for('index'))
	if handover_hash is not None and handover.access_hash == handover_hash:
		editable = True
		form.email.data = user.email 
		form.text.data = text[0].text
		form.name.data = user.name
	else: 
		editable = False
	if form.validate_on_submit():
		user.email = form.email.data
		if handover.media_id != None:
			media = Media.query.get(handover.media_id)
		db.session.commit()
	return render_template('handover.html',title = "Show Handover", form = form, editable = editable, handover = handover, text=text[0], username = user.name, email = user.email, artifact_id = handover.artifact_id, handover_count = handover_count)


