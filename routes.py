from flask import Blueprint, flash
from flask import request, render_template, redirect, url_for

from models import User
from datetime import datetime

main = Blueprint("main", __name__)

posts = []

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

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'username' in request.form and 'post' in request.form:
            username = request.form['username']
            post = request.form['post']
            posts.append({
                'username': username,
                'post': post,
                'date': datetime.now()
            })
            print(posts)
            redirect('/')
    return render_template('index.html', posts = posts )


@main.route('/home', methods=['GET', 'POST'])
def home():
    
    return render_template('home.html')
