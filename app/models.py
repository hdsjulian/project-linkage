from app import db
from datetime import datetime

import enum
import uuid

class MediaType(enum.Enum):
	image = 'Image'
	text = 'Text'
	blob = 'Blob'


class User(db.Model): 
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(128), index=True)
	access_hash = db.Column(db.String(32), default=uuid.uuid4().hex)
	handovers = db.relationship('Handover', backref='recipient')
	def __init__(self, email):
		self.email=email

	@classmethod
	def get_or_create_user(cls, email):
		user = db.session.query(User).filter_by(email=email).first()
		if user: 
			return user
		else: 
			user = User(email)
			db.session.add(user)
			db.session.commit()
			return user

class Artifact(db.Model): 
	id = db.Column(db.Integer, primary_key=True)
	access_hash = db.Column(db.String(32), default=uuid.uuid4().hex)
	handovers = db.relationship('Handover', backref='artifact') 
	rules = db.relationship('Rule', backref='rule')

class Handover(db.Model): 
	id = db.Column(db.Integer, primary_key=True)
	access_hash = db.Column(db.String(32), default=uuid.uuid4().hex)
	artifact_id = db.Column(db.Integer, db.ForeignKey('artifact.id'))
	predecessor_id = db.Column(db.Integer, db.ForeignKey('handover.id')) 
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	media_id = db.Column(db.Integer, db.ForeignKey('media.id'))
	date = db.Column(db.DateTime, index=True, default = datetime.utcnow)
	lat = db.Column(db.Float)
	lon = db.Column(db.Float)
	predecessor = db.relationship('Handover', backref=db.backref('previous', remote_side=id))

class Rule(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.Text)
	date = db.Column(db.DateTime, index = True, default = datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	applies_to = db.Column(db.Integer, db.ForeignKey('artifact.id'))

class Media(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	type = db.Column(db.Enum(MediaType))
	texts = db.relationship('Text', backref='texts')


class Text(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	text = db.Column(db.Text)
	date = db.Column(db.DateTime, index = True, default = datetime.utcnow)
	media_id = db.Column(db.Integer, db.ForeignKey('media.id'))




