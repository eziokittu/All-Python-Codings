from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMT_DATABASE_URI"] = "sqlite:///mywebside.dp"
app.config["SQLALCHEMT_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class MyApp(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.Integer, primary_key = True)
    sno = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route("/")
def hello_world():
    #return "<l1>Hello, World!</l1><l2>\nHi</l2>"
    return render_template("WebPage1.html")

@app.route("/products/")
def products():
    return "This is products page"

if __name__ == "__main__":
    app.run(debug = True, port=1000)