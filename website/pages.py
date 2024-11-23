from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify, session
from flask_login import login_required, current_user
from .models import db, User #, Stats

pages = Blueprint("pages", __name__)

@pages.route('/')
@pages.route('/home')
def home():
    if current_user.is_authenticated:
        return render_template('index.html', user=current_user) 
    else:
        return render_template('welcome.html', user=current_user)

