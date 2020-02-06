from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, TextAreaField, HiddenField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    name = StringField('Please enter a name (not necessary)')
    email = StringField('Enter your e-mail-address (necessary)', validators=[DataRequired()])
    text = TextAreaField('Write something about your handover. Or save it for later.')
    lat = HiddenField('lat', validators=[DataRequired()], default=10)
    lon = HiddenField('lon', validators=[DataRequired()], default=10)
    submit = SubmitField('Register')

class UpdateForm(FlaskForm):
    name = StringField('Please enter a name (not necessary)')
    email = StringField('Enter your e-mail-address (necessary)', validators=[DataRequired()])
    text = TextAreaField('Write something about your handover. Or save it for later.')
    lat = HiddenField('lat', validators=[DataRequired()], default=10)
    lon = HiddenField('lon', validators=[DataRequired()], default=10)
    handover_id = HiddenField('handover_id', validators=[DataRequired()])
    submit = SubmitField('Register')
