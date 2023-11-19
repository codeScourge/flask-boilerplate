from flask import Flask, render_template
import werkzeug
import json
import random

from blueprints.api.api_bp import api_bp

MESSAGES = ["Flask is the new NextJS", "Serverside rendering is not JS only", "Python > JS"]

app = Flask(__name__)
app.config.from_file("flask_config.json", load=json.load)
app.register_blueprint(api_bp, url_prefix="/api")

# @app.errorhandler(werkzeug.exceptions.HTTPException)
# def handleHTTPException(error):
#     app.logger.error(error.description)
#     return {"message": error.description}, error.code


@app.errorhandler(404)
def routerRoute(error):
    return render_template("home.html", message=random.choice(MESSAGES))

@app.route("/", methods=["GET"])
def homeRoute():
    return render_template("home.html", message=random.choice(MESSAGES))

