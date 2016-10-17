from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
								Length, EqualTo)
from wtfpeewee.orm import model_form

from models import User


# Validator methods
def name_exists(form, field):
	if User.select().where(User.username == field.data).exists():
		raise ValidationError("User with that name already exists.")

def email_exists(form, field):
	if User.select().where(User.email == field.data).exists():
		raise ValidationError("User with that email already exists.")


class RegisterForm(FlaskForm):
	username = StringField(
		'Username',
		validators=[
			DataRequired(),
			Regexp(
				r'^[a-zA-Z0-9_]+$',
				message=("Username should be one word, letters, "
				"numbers, and underscores only.")
			),
			name_exists
	])
	email = StringField(
		'Email',
		validators=[
			DataRequired(),
			Email(),
			email_exists
	])
	password = PasswordField(
		'Password',
		validators=[
			DataRequired(),
			Length(min=2),
			EqualTo('password2', message='Passwords must match.')
	])
	password2 = PasswordField(
		'Confirm Password',
		validators=[DataRequired()]
	)


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])


class PostForm(FlaskForm):
	content = TextAreaField("What's up?", validators=[DataRequired()])


UserProfileUpdateForm = model_form(User, 
	exclude=['password', 'joined_at', 'is_admin'],
	field_args={
		'username': {'label': 'Username'},
		'email': {'label': 'Email Address'}
	})