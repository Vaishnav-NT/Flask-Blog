import os
##import secrets
##from PIL import Image
from flask import url_for, current_app
##from flask_mail import Message
##from flaskblog import mail


def save_picture(form_picture):
    random_hex = "";
    f_name , f_ext = os.path.splitext(form_picture.filename)
    picture_fn = f_name + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    form_picture.save(picture_path)
    return picture_fn