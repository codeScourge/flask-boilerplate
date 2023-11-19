from flask import Flask, render_template
import werkzeug
import json

app = Flask(__name__)
app.config.from_file("config.json", load=json.load)

@app.errorhandler(werkzeug.exceptions.HTTPException)
def handleHTTPException(error):
    app.logger.error(error.description)
    return {"message": error.description}, error.code

@app.route("/", methods=["GET"])
def homeRoute():
    return render_template("home.html")

@app.route("/ping", methods=["GET"])
def pingRoute():
    return {"message": "PONG"}, 200
