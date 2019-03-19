from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UserForm(FlaskForm):
  fname = StringField('First Name', validators=[DataRequired()])
  lname = StringField('Last Name', validators=[DataRequired()])
  gender = SelectField('Gender', choices=[('Male','Male'),('Female', 'Female')], validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  location = StringField('Location', validators=[DataRequired()])
  bio = TextAreaField('Biography', validators=[DataRequired()])
  photo = FileField('Profile Picture', validators=[FileRequired(), FileAllowed(['jpg','png','Images Only!'])])
