from flask import Flask, request
from app.controllers.shortener_controller import ShortenerController


app = Flask(__name__)
shortenerController = ShortenerController()


@app.route('/', methods=['GET', 'POST'])
def index():
    """Returns the index page"""

    # If GET request, return index page.
    if request.method == 'GET':
        return shortenerController.index()

    # If POST request, create short URL.
    if request.method == 'POST':
        return shortenerController.postUrl(request.form['url'])