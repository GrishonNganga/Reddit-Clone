from flask import Blueprint, flash
from flask import request, render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from models import User, Post, mysql
from reddit import manager

from datetime import datetime

main = Blueprint("main", __name__)

posts = []

@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@main.route('/register', methods=['GET','POST'])
def register_user():
    if request.method == 'POST':
        form = request.form
        username = form.get("username")
        password = form.get("password")
        confirm_password = form.get("confirmpassword")
        if username is None or password is None  or confirm_password is None:
            error = 'username, email, password are required'
            flash(error)
            return render_template('signup.html', error=error)
        if ' ' in username:
            error = 'Username should not contain spaces'
            flash(error)
            return render_template('signup.html', error=error)
        if password != confirm_password:
            error = "Passwords do not match"
            flash(error)
            return render_template('signup.html', error=error)
        else:
            user = User.query.filter_by(username=username).first()
            if user is not None:
                error = 'A user with that name already exists'
                flash(error)
                return render_template('signup.html', error=error)
            
            user = User(username=username)
            user.set_password(password)
            user.save()
            return redirect(url_for('main.index'))

    return render_template('signup.html')

@main.route('/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        form = request.form
        username = form.get("username")
        password = form.get("password")
        if username is None or password is None:
            error = 'username, email, password are required'
            flash(error)
            return render_template('signup.html', error=error)
        else:
            user = User.query.filter_by(username=username).first()
            if user is None:
                error = 'A user with that username  does not exist'
                return render_template('login.html', error=error)
            is_correct_password = user.check_password(password)
            print(is_correct_password)
            if not is_correct_password:
                error = 'Username or password not correct.'
                flash(error)
                return render_template('signup.html', error=error)
            
            login_user(user)
            return redirect(url_for('main.index'))
    return render_template('signup.html')

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.register_user'))

@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        if 'post' in request.form:
            username = current_user.id
            post = request.form['post']
            # posts.append({
            #     'username': username,
            #     'post': post,
            #     'date': datetime.now()
            # })
            post = Post(body = post, user_id = current_user.id)
            mysql.session.add(post)
            mysql.session.commit()
            redirect('/')
    posts = Post.query.all()
    return render_template('index.html', posts = posts)


@main.route('/home', methods=['GET', 'POST'])
def home():
    
    return render_template('home.html')
