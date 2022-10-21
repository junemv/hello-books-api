from flask import Blueprint, jsonify

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

class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
    Book(2, "The Prince and the Dressmaker", "A story about the seamstress who makes dresses for her prince."),
    Book(3, "Lost at Sea", "The story of a girl, Riley, who finds herself on a roadtrip with a car- full of strangers.")
] 

books_bp = Blueprint("books", __name__, url_prefix="/books")
@books_bp.route("", methods = ['GET'])
def handle_books():
    books_result = []
    for book in books:
        books_result.append({
            'id': book.id,
            'title': book.title,
            'description': book.description
        })
    return jsonify(books_result)

@books_bp.route("/<book_id>", methods=["GET"])
def handle_book(book_id):
    book_id = int(book_id)
    for book in books:
        if book.id == book_id:
            return {
                "id": book.id,
                "title": book.title,
                "description": book.description,
            }

    return {"message":f"book {book_id} not found"}, 404