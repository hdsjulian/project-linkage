from app import db
from datetime import datetime
import enum

class MediaType(enum.Enum):
	image = 'Image'
	text = 'Text'


class User(db.Model): 
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(128), index=True)
	access_hash = db.Column(db.String(128))
	handovers = db.relationship('Handover', backref='recipient')

class Artifact(db.Model): 
	id = db.Column(db.Integer, primary_key=True)
	handovers = db.relationship('Handover', backref='artifact') 
	rules = db.relationship('Rule', backref='rule')

class Handover(db.Model): 
	id = db.Column(db.Integer, primary_key=True)
	artifact_id = db.column(db.Integer, db.ForeignKey('artifact.id'))
	predecessor_id = db.column(db.Integer, db.ForeignKey('handover.id')) 
	user_id = db.column(db.Integer, db.ForeignKey('user.id'))
	media_id = db.column(db.Integer, db.ForeignKey('media.id'))
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
	type = db.column(db.Enum(MediaType))
	texts = db.relationship('Texts', backref='texts')


class Texts(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	text = db.column(db.Text)
	date = db.Column(db.DateTime, index = True, default = datetime.utcnow)
	media_id = db.Column(db.Integer, db.ForeignKey('media.id'))


	

