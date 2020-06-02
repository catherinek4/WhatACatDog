# Python standard libraries
import json
import os
import sqlite3

# Third party libraries
from flask import Flask, redirect, request, url_for, render_template
import requests
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
# Internal imports
from db import init_db_command
from user import User
import app

# Flask-Login helper to retrieve a user from our db
#@login_manager.user_loader
def load_user(user_email):
    return User.getByEmail(user_email)

def login(user_name, user_email, user_password):
    if User.getByEmail(user_email):
	    return render_template('main.html', errorSignUp="User with this email already exists")
    # Doesn't exist? Add to database
    User.createByForm(user_name, user_email, user_password)
	
    user = User.getByEmail(user_email)
    # Begin user session by logging the user in
    login_user(user)

    # Send user back to homepage
    return render_template('main.html')
    #return redirect(url_for("index"))
