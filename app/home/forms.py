from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms import ValidationError

# alternative way of using form , refactor later
class ContactForm(FlaskForm):
    pass


class UploadForm(FlaskForm):
    uploadfile = FileField(validators=[FileRequired()])
    submit = SubmitField("Submit")
