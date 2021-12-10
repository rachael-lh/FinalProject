from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask (__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:MYPASSWORD@db:3306/MySQLDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Users(db.Model):
    full_name = db.Column(db.String(100), primary_key = True, nullable=False)
    #email = db.Column(db.String(100), nullable=False)
    user_password = db.Column(db.String(100), nullable=False)
    goals_relationship = db.relationship('usergoals', backref='users', lazy=True)
    def __init__(self, full_name, user_password):
        self.full_name = full_name
        #self.email = email
        self.user_password = user_password

class usergoals(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    goals = db.Column(db.String(100), nullable=False)
    date_started = db.Column(db.String(100), nullable=False)
    date_endgoal = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), db.ForeignKey('users.full_name'), nullable=False) 
    def __init__(self, goals, date_started, date_endgoal, username):
        self.goals = goals
        self.date_started = date_started
        self.date_endgoal = date_endgoal
        self.username = username

@app.route('/')
def index():
    users_data = Users.query.all()
    usergoals_data = usergoals.query.all()
    return render_template("index.html", users = users_data, goals = usergoals_data)

@app.route('/update', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = usergoals.query.get(request.form.get('id'))

        my_data.goals = request.form['goals']
        my_data.date_started = request.form['date_started']
        my_data.date_endgoal = request.form['date_endgoal']

        db.session.commit()
        flash("User information updated successfully!")

        return redirect(url_for('index'))

@app.route('/insert', methods = ['POST'])
def insert():
    
    if request.method == 'POST':
        exists = db.session.query(Users.full_name).filter_by(full_name=request.form['username']).scalar() is not None
        if exists == True:
 

            goals = request.form['goals']
            date_started = request.form['date_started']
            date_endgoal = request.form['date_endgoal']
            username = request.form['username']

            my_data = usergoals(goals, date_started, date_endgoal, username)
            db.session.add(my_data)
            db.session.commit()
 
            flash("Details inserted successfully")
            return redirect(url_for('index'))
        else:
            full_name = request.form['username']
            my_data = Users(full_name,'ergrgh')
            db.session.add(my_data)
            db.session.commit()

            goals = request.form['goals']
            date_started = request.form['date_started']
            date_endgoal = request.form['date_endgoal']
            username = request.form['username']

            my_data = usergoals(goals, date_started, date_endgoal, username)
            db.session.add(my_data)
            db.session.commit()
 
            flash("Details inserted successfully")
            return redirect(url_for('index'))




@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = usergoals.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("User Deleted Successfully")

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)