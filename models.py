from flask_sqlalchemy import SQLAlchemy

mysql = SQLAlchemy()

class User(mysql.Model):
    id = mysql.Column(mysql.Integer, primary_key = True) 
    username = mysql.Column(mysql.String(50), nullable = False)
    password = mysql.Column(mysql.String(200), nullable = False)

    def save(self):
        mysql.session.add(self)
        mysql.session.commit()

    #TODO Add the rest of the methods (Password Hashing, Password Unhashing) 


class Post(mysql.Model):
    id = mysql.Column(mysql.Integer, primary_key = True)
    body = mysql.Column(mysql.String(1001), nullable = False)