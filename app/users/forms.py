from flask_wtf import Form
from wtforms import TextField, DateField, IntegerField, SelectField, PasswordField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegisterForm(Form):
	name = TextField('Username', validators=[DataRequired(), Length(min=4, max=25)])
	email = TextField('Email', validators=[DataRequired(), Length(min=6, max=40)])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=40)])
	confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('Password', message='Passwords must match')])

class LoginForm(Form):
	name = TextField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])