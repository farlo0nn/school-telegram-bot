from flask import Flask
from settings import ADMIN_SECRET_KEY


UPLOAD_FOLDER = './templates/images/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__,template_folder='./templates',static_folder='./static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = ADMIN_SECRET_KEY

import admin.views
