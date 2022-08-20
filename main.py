from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://uuxhuzlobmhwjp:8b98a5e5c7665df1c0058e01adf0748c377d1c1eb4163a11d94c524d80abeccc@ec2-3-209-124-113.compute-1.amazonaws.com:5432/daqt83fsalutsp'
db = SQLAlchemy(app)

class Item(db.Model):
    name = db.Column(db.String(length=30))







@app.route('/')
def hello_world():
    return render_template('home.html');

