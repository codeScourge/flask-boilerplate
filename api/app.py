from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics
from flask import Flask, render_template

app = Flask(__name__)
metrics = GunicornInternalPrometheusMetrics(app)

@app.route("/ping", methods=["GET"])
def pingRoute():
    return {"message": "PONG"}, 200

@app.route("/", methods=["GET"])
def homeRoute():
    return render_template("home.html")
