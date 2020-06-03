# Python standard libraries
import json
import os

# Third party libraries
from flask import Flask, render_template

# Internal imports
from user import User
import app

def load_user(user_email):
    return User.getByEmail(user_email)

def login(user_name, user_email, user_password):
    if User.getByEmail(user_email):
	    return render_template('main.html', errorSignUp="User with this email already exists")
    User.createByForm(user_name, user_email, user_password)	
    user = User.getByEmail(user_email)
    return user
