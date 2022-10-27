from app import db
from app.models.book import Book
from flask import abort, Blueprint, jsonify, make_response, request

books_bp = Blueprint("books", __name__, url_prefix="/books")
@books_bp.route("", methods=["POST"])
def create_book():
    '''
    POST method - allows user to add a book and its corresponding parameters
    to the book's record
    '''
    request_body = request.get_json()
    new_book = Book(title=request_body["title"],
                    description=request_body["description"])

    db.session.add(new_book)
    db.session.commit()

    return make_response(f"Book {new_book.title} successfully created", 201)

@books_bp.route("", methods=["GET"])
def read_all_books():
    '''
    GET method - allows user to query all book records from book table
    '''
    books = Book.query.all()
    books_response = []
    for book in books:
        books_response.append({
            'id': book.id,
            'title': book.title,
            'description': book.description
        })
    return jsonify(books_response)

def validate_book(book_id):
    '''
    helper function - throws an error with http code for invalid book IDs
    '''
    try:
        book_id = int(book_id)
    except:
        abort(make_response({"message":f"book {book_id} invalid"}, 400))
    
    book = Book.query.get(book_id)
    
    if not book:
        abort(make_response({"message":f"book {book_id} not found"}, 404))
    return book

@books_bp.route("", methods=['GET'])
def read_one_book(book_id):
    '''
    GET method - allows user to query one book's record from book table
    '''
    book = validate_book(book_id)

    return {
        'id': book.id,
        'title': book.title,
        'description': book.description
    }











# hello_world_bp = Blueprint("hello_world", __name__)

# @hello_world_bp.route("/hello-world", methods=["GET"])
# def say_hello_world():
#     response_body = "Hello, World!"
#     return response_body, 200

# @hello_world_bp.route("/hello/JSON", methods=["GET"])
# def say_hello_json():
#     return {
#         "name": "June Valentino",
#         "message": "I'm sleepy.",
#         "hobbies": ["Video Games", "Art", "Animation"]
#     }


# @hello_world_bp.route("/fixed-endpoint-with-fixed-server-code")
# def broken_endpoint():
#     response_body = {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }
#     new_hobby = "Surfing"
#     response_body["hobbies"].append(new_hobby)
#     return response_body

# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# books = [
#     Book(1, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
#     Book(2, "The Prince and the Dressmaker", "A story about the seamstress who makes dresses for her prince."),
#     Book(3, "Lost at Sea", "The story of a girl, Riley, who finds herself on a roadtrip with a car- full of strangers.")
# ] 

# books_bp = Blueprint("books", __name__, url_prefix="/books")
# @books_bp.route("", methods = ['GET'])
# def handle_books():
#     books_result = []
#     for book in books:
#         books_result.append({
#             'id': book.id,
#             'title': book.title,
#             'description': book.description
#         })
#     return jsonify(books_result)

# @books_bp.route("/<book_id>", methods=["GET"])
# def handle_book(book_id):
#     book = validate_book(book_id)
    
#     return {
#         "id": book.id,
#         "title": book.title,
#         "description": book.description,
#     }
