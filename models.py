from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
mysql = SQLAlchemy()

class User(UserMixin, mysql.Model):
    id = mysql.Column(mysql.Integer, primary_key = True) 
    username = mysql.Column(mysql.String(50), nullable = False)
    password = mysql.Column(mysql.String(200), nullable = False)

    def save(self):
        mysql.session.add(self)
        mysql.session.commit()

    def set_password(self, password):
        pass_hash = generate_password_hash(password)
        self.password = pass_hash

    def check_password(self, password):
        return check_password_hash(self.password, password)

    #TODO Add the rest of the methods (Password Hashing, Password Unhashing) 


class Post(mysql.Model):
    id = mysql.Column(mysql.Integer, primary_key = True)
    body = mysql.Column(mysql.String(1001), nullable = False)