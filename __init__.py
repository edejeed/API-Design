from flask import Flask, jsonify, request
import psycopg2

# Database connection

db_connection = psycopg2.connect(
        dbname='api',
        user='postgres',
        password='helloworld',
        host='localhost',
    )

app = Flask(__name__)

# Sample data
books = [
    {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
]

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({"status": "ok",
                    'books': books})

# Get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((item for item in books if item['id'] == book_id), None)
    if book:
        return jsonify({"status": "ok",
                        'book': book})
    else:
        return jsonify({"status": "error",
                        'message': 'Book not found'})

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    new_book = {'id': len(books) + 1, 'title': request.json['title'], 'author': request.json['author']}
    books.append(new_book)
    return jsonify({"status": "ok",
                    'message': 'Book created successfully', 'book': new_book})

# Update a book by ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((item for item in books if item['id'] == book_id), None)
    if book:
        book['title'] = request.json.get('title', book['title'])
        book['author'] = request.json.get('author', book['author'])
        return jsonify({"status": "ok",
                        'message': 'Book updated successfully', 'book': book})
    else:
        return jsonify({"status": "error",
                        'message': 'Book not found'})

# Delete a book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [item for item in books if item['id'] != book_id]
    return jsonify({"status": "ok",
                    'message': 'Book deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
