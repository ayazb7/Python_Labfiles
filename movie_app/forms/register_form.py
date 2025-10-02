from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField

class RegisterForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Register')