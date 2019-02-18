from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ContactForm(Form):
    name = StringField('Name:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired()])
    subject = StringField('Subject:', validators=[DataRequired()])
    message = TextAreaField('Message:', validators=[DataRequired()])
    send = SubmitField("Send")