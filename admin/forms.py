from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, SelectField, Field
from wtforms.validators import DataRequired

class LessonAddForm(FlaskForm):
    name = StringField("Username", validators=[DataRequired()])
    link = StringField("Meeting Link", validators=[DataRequired()])
    meeting_id = StringField("Meeting ID", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    teacher = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

class LessonEditForm(FlaskForm):
    original_name = StringField("Name")
    changed_name = StringField("Name Changed", validators=[DataRequired()])
    link = StringField("Meeting Link", validators=[DataRequired()])
    meeting_id = StringField("Meeting ID", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    teacher = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

class ModelEditOptionsForm(FlaskForm):
    model = SelectField('Choose Model To Edit', choices=['User','Lesson'], validators=[DataRequired()], default=None)
    submit = SubmitField("Submit")

class LessonOptionsEditForm(FlaskForm):
    lesson_operation = SelectField("Choose Operation", choices=['Add','Delete','Edit'], validators=[DataRequired()])
    submit = SubmitField("Submit")

class UserEditOptionsForm(FlaskForm):
    user_operation = SelectField("Choose Operation", choices=['Add','Delete'], validators=[DataRequired()])
    submit = SubmitField("Submit")

class UserAddForm(FlaskForm):
    chat_id = IntegerField("Chat ID", validators=[DataRequired()])
    submit = SubmitField("Submit")

class UserDeleteForm(FlaskForm):
    username = SelectField("Chat ID", choices=[], validators=[DataRequired()])
    submit = SubmitField("Submit")

# class LessonForm(FlaskForm):
#     option = StringField(default='Delete')
#     lessonsNames = SelectField("Category", choices=[], validators=[DataRequired()])
#     submit = SubmitField("Submit")

class LessonDeleteForm(FlaskForm):
    name = SelectField(choices=[], validators=[DataRequired()])
    submit = SubmitField("Submit")

class LessonChooseForm(FlaskForm):
    name = SelectField(choices=[], validators=[DataRequired()])
    submit = SubmitField("Submit")