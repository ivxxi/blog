from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,SubmitField,TextAreaField,RadioField, SelectField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError

class EditProfileForm(FlaskForm):
    username = StringField('Username',validators=[Required()])
    about_me = TextAreaField('About me', validators=[Required()])
    submit = SubmitField('Submit')

    #def __init__(self, original_username, *args, **kwargs):
    #    super(EditProfileForm, self).__init__(*args, **kwargs)
    #    self.original_username = original_username

    #def validate_username(self, username):
    #    if username.data != self.original_username:
    #        user = User.query.filter_by(username=self.username.data).first()
    #        if user is not None:
    #            raise ValidationError('Please use a different username.')


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    post = TextAreaField('Blog Content',validators=[Required()])
    submit = SubmitField('Submit')
