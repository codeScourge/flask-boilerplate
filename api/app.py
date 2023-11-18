from flask import Flask, render_template

app = Flask(__name__)

@app.route("/ping", methods=["GET"])
def pingRoute():
    return {"message": "PONG"}, 200

@app.route("/", methods=["GET"])
def homeRoute():
    return render_template("home.html")
