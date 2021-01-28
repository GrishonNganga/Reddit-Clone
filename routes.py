from flask import Blueprint
from flask import request, render_template, redirect

from datetime import datetime

main = Blueprint("main", __name__)

posts = []

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
