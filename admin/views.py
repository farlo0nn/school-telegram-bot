from flask import render_template, redirect, request, url_for, flash
from . import app
from .forms import \
    LessonDeleteForm, LessonOptionsEditForm, LessonAddForm, \
    UserEditOptionsForm, UserAddForm, ModelEditOptionsForm, \
    UserDeleteForm, LessonEditForm, LessonChooseForm
from db.db import session
from db.models import User, Lesson
from db.utils import addUser
from services.bot.utils import getUserInfoByChatId
from logger.logger import logger

@app.route('/', methods=['POST','GET'])
def home():

    usersNames=[user.username for user in session.query(User).all()]
    lessons=session.query(Lesson).all()
    lessonsNames=[lesson.name for lesson in lessons]

    lessonChooseForm = LessonChooseForm()
    modelEditOptionsForm = ModelEditOptionsForm()
    lessonOptionsEditForm = LessonOptionsEditForm()
    lessonDeleteForm = LessonDeleteForm()
    lessonAddForm = LessonAddForm()
    lessonEditForm = LessonEditForm()
    lessonToEdit = None

    userAddForm = UserAddForm()    
    userDeleteForm = UserDeleteForm()
    userEditOptionsForm = UserEditOptionsForm()

    userDeleteForm.username.choices = usersNames

    lessonOptionsEditForm.lesson_operation.choices = ['Add','Delete']+[f'Edit {lesson.name}' for lesson in lessons]
    # lessonEditForm.lesson.choices = lessons
    lessonDeleteForm.name.choices = lessonsNames
    lessonChooseForm.name.choices = lessonsNames

    if userEditOptionsForm.validate_on_submit():
        logger.debug(userEditOptionsForm.user_operation.data)
        
    if userAddForm.validate_on_submit():
        userInfo = getUserInfoByChatId(userAddForm.chat_id.data)
        addUser(userInfo)

    if userDeleteForm.validate_on_submit():
        user = session.query(User).filter_by(username=userDeleteForm.username.data).first()
        session.delete(user)
        session.commit()

    if lessonDeleteForm.validate_on_submit():
        lessonToDelete: Lesson = session.query(Lesson).filter_by(name=lessonDeleteForm.name.data)
        session.delete(lessonToDelete)
        session.commit()

    if lessonOptionsEditForm.validate_on_submit():
        lessonToEdit: Lesson = session.query(Lesson).filter_by(name=lessonOptionsEditForm.lesson_operation.data.split()[1]).first()
        
    if lessonEditForm.validate_on_submit():
        logger.debug('LessonEditForm is submitted')
        lessonToEdit: Lesson = session.query(Lesson).filter_by(name=lessonEditForm.original_name.data).first()
        logger.debug(lessonToEdit.name)
        lessonToEdit.name=lessonEditForm.changed_name.data
        lessonToEdit.meeting_id=lessonEditForm.meeting_id.data
        lessonToEdit.password=lessonEditForm.password.data
        lessonToEdit.link=lessonEditForm.link.data
        lessonToEdit.teacher=lessonEditForm.teacher.data

        logger.info(f'Lesson {lessonEditForm.original_name.data} is Edited, {lessonToEdit.name}|{lessonToEdit.link}|{lessonToEdit.meeting_id}|{lessonToEdit.password}|{lessonToEdit.teacher}')
    
        lessons=session.query(Lesson).all()
        lessonsNames=[lesson.name for lesson in lessons]
    
        lessonOptionsEditForm.lesson_operation.choices = [f'Edit {lesson.name}' for lesson in lessons]
        # lessonEditForm.lesson.choices = lessons
        lessonDeleteForm.name.choices = lessonsNames
        lessonChooseForm.name.choices = lessonsNames

        session.commit()


    if lessonAddForm.validate_on_submit():
        ...
    # if lessonForm.validate_on_submit():
    #     if not session.query(Lesson).filter_by(name=lessonForm.name.data).first():
    #         lesson = Lesson(
    #             name=lessonForm.name.data,
    #             link=lessonForm.link.data,
    #             meeting_id=lessonForm.meeting_id.data,
    #             password=lessonForm.password.data,
    #             teacher=lessonForm.teacher.data
    #         )
    #         try:
    #             session.add(lesson)
    #             session.commit()
    #         except Exception as ex:
    #             session.rollback()
    #             logger.debug(ex)
            
    #     # lessonForm = LessonForm()

    # if userForm.validate_on_submit(): 
    #     user = session.query(User).filter_by(chat_id=userForm.chat_id.data).first()
    #     if user is None:
    #         userInfo = getUserInfoByChatId(userForm.chat_id.data)
    #         if userInfo is not None:
    #             addUser(userInfo)
    #         userForm = UserForm()

    return render_template(
        'home.html', 
        modelEditOptionsForm=modelEditOptionsForm,
        lessonOptionsEditForm=lessonOptionsEditForm,
        userEditOptionsForm=userEditOptionsForm,
        lessonDeleteForm=lessonDeleteForm,
        lessonAddForm=lessonAddForm,
        lessonEditForm=lessonEditForm, 
        userAddForm=userAddForm,
        userDeleteForm=userDeleteForm,
        lessonChooseForm=lessonChooseForm,
        lessonToEdit=lessonToEdit
    )


