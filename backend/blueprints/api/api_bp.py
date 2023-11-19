# Blueprint for the api routes
from flask import Blueprint

api_bp = Blueprint("api_bp", __name__)

@api_bp.get("/double/<int:num>")
def doubleRoute(num):
    return {"result": num * 2}
