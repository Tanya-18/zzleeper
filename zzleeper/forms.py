from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, InputRequired
from email_validator import validate_email


class RegistrationForm(FlaskForm):
    email = StringField('Email',
                validators=[InputRequired("Please enter your email address."), 
                Email("Enter valid email address")])
    username =  StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email',
                validators=[InputRequired("Please enter your email address."), 
                Email("Enter valid email address")])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')    


