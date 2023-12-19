from flask import Flask, render_template
from .blueprints import api_bp
import serverless_wsgi
import random
import json

MESSAGES = ["Flask is the new NextJS", "Serverside rendering is not JS only", "Python > JS"]

app = Flask(__name__)
app.config.from_file("flask_config.json", load=json.load)
app.register_blueprint(api_bp, url_prefix="/api")

@app.errorhandler(404)
def routerRoute(error):
    return render_template("home.html", message=random.choice(MESSAGES))

@app.route("/", methods=["GET"])
def homeRoute():
    return render_template("home.html", message=random.choice(MESSAGES))

def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)
