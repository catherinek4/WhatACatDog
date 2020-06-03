# Python standard libraries
import json
import os

# Third party libraries
from flask import Flask, render_template

# Internal imports
from user import User
import app

def login(user_email, user_password):
    user = User.get(user_email, user_password)
    if user is None:
	    return render_template('main.html', errorSignIn="error while login")
    return user
