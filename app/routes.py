from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route("/hello-world", methods=["GET"])
def say_hello_world():
    response_body = "Hello, World!"
    return response_body, 200

@hello_world_bp.route("/hello/JSON", methods=["GET"])
def say_hello_json():
    return {
        "name": "June Valentino",
        "message": "I'm sleepy.",
        "hobbies": ["Video Games", "Art", "Animation"]
    }

@hello_world_bp.route("/fixed-endpoint-with-fixed-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby)
    return response_body