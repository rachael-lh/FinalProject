from flask import Flask

app = Flask (__name__)

@app.route('/')
def index():
    goals_list = "Goals list innit"
    return goals_list

if __name__ == "__main__":
    app.run(debug=True)