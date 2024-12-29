from flask import flash, Blueprint, redirect, render_template, request, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    data=request.form
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return render_template("home.html")

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method=='POST':
        email=request.form.get('email', '')
        first_name=request.form.get('firstName', '') # should match the name in html form of GET
        pwd1=request.form.get('password1', '')
        pwd2=request.form.get('password2', '')
        print(f"Email: {email}")
        print(f"First Name: {first_name}")
        print(f"Password1: {pwd1}")
        print(f"Password2: {pwd2}")
        if len(email) < 4:
            flash('Email id is too short, must be greater than 4 characters', category = 'error')
        elif len(first_name) < 2: 
            flash('First name should be greater than 2 characters', category = 'error')
        elif pwd1 != pwd2:
            flash('Passwords does not match!', category = 'error')
        else:
            new_user = User(email=email, password=generate_password_hash(pwd1, method='pbkdf2:sha256'), first_name=first_name)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")
