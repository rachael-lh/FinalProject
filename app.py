from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)
app.secret_key = "Secret Key"

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'rachael',
    'database': 'test'
}
db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

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


@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)