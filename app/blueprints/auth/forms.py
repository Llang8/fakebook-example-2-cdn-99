from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class SignupForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    username = StringField('Username', validators = [DataRequired()])
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    password = PasswordField('Password', validators= [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit_button = SubmitField('Create my Account')