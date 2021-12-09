from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:MYPASSWORD@db:3306/MySQLDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    user_password = db.Column(db.String(100), nullable=False)
    def __init__(self, full_name, email, user_password):
        self.full_name = full_name
        self.email = email
        self.user_password = user_password

class User_Goals(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    _id = db.Column(db.Integer)
    Goal = db.Column(db.String(100))
    Date_Started = db.Column(db.String(100))
    Date_Endgoal = db.Column(db.String(100))
    def __init__(self, Goal, Date_Started, Date_Endgoal):
        self.Goal = Goal
        self.Date_Started = Date_Started
        self.Date_endgoal = Date_Endgoal

@app.route('/')
def index():
    all_data = Users.query.all()

    return render_template("index.html", users = all_data)

@app.route('/update', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = Users.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.email = request.form['email']
      #  my_data.password = request.form['password']

        db.session.commit()
        flash("User information updated successfully!")

        return redirect(url_for('index'))

@app.route('/insert', methods = ['POST'])
def insert():
 
    if request.method == 'POST':
 
        name = request.form['name']
        Goals = request.form['goals']
        Date_Started = request.form['datestarted']
        Date_endgoal = request.form['dateend']
 
        my_data = Users(name)
        my_data = User_Goals(Goals, Goals, Date_Started, Date_endgoal)
        db.session.add(my_data)
        db.session.commit()
 
        flash("Details inserted successfully")
        return redirect(url_for('index'))



@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Users.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("User Deleted Successfully")

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
