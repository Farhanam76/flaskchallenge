from flask import Flask, request, jsonify

app = Flask(__name__)


books = []


def add_book():
    '''
    Add a new book to the list

    Parameters:
    Title (str): The title of the book
    Author (str): The name of the author of the book
    Pages (int): The number of pages of the book
    Genre (str): The genre of the book
    IBSN (int): The International Standard Book Number of the book

    Return:
    dict: A dictionary that contains details of the added book
    '''
    
    title = request.args.get('title')
    author = request.args.get('author')
    pages = int(request.args.get('pages'))
    genre = request.args.get('genre')
    isbn = int(request.args.get('isbn'))

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
    '''
    Search for books by the author's name

    parameters
    author(str): The author's name
    return: 
    list: A list of dictionaries containing book details matching the given author's name.
    '''
    
    
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
