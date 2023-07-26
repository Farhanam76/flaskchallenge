from flask import Flask, request, jsonify

app = Flask(__name__)


books = []


def add_book():
    title = request.args.get('title')
    author = request.args.get('author')
    pages = int(request.args.get('pages'))
    genre = request.args.get('genre')
    isbn = request.args.get('isbn')

    if not (title and author and pages and genre and isbn):
        return "Invalid data. Please provide all book details."

    new_book = {
        'title': title,
        'author': author,
        'pages': pages,
        'genre': genre,
        'isbn': isbn
    }

    books.append(new_book)

    return {"message": "Book added successfully", "book": new_book}


def search_books_by_author():
    author = request.args.get('author')

    if not author:
        return "Invalid data. Please provide the author's name."

    result = [book for book in books if book['author'].lower() == author.lower()]

    if not result:
        return "No books found for the given author."
    else:
        return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
