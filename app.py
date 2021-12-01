from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:rachael@127.0.0.1:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User_Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

class User_Goals(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Goal = db.Column(db.String(100))
    Date_Started = db.Column(db.String(100))
    Date_Endgoal = db.Column(db.String(100))

    def __init__(self, Goal, Date_Started, Date_Endgoal):
        self.Goal = Goal
        self.Date_Started = Date_Started
        self.Date_endgoal = Date_Endgoal

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/insert', methods = ['POST'])
def insert():
 
    if request.method == 'POST':
 
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
 
 
        my_data = User_Data(name, email, phone)
        db.session.add(my_data)
        db.session.commit()
 
        flash("Details inserted successfully")
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)