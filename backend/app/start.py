import os

import redis
from flask import Flask, request, render_template

from app.controllers.shortener_controller import ShortenerController


r = redis.Redis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'], db=os.environ['REDIS_DB'])
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Handles requests to /"""

    shortenerController = ShortenerController(r)

    # If GET request, return index page.
    if request.method == 'GET':
        return shortenerController.index()

    # If POST request, create short URL.
    if request.method == 'POST':
        return shortenerController.post_url(request.form['url'])


@app.route('/<short_id>', methods=['GET'])
def redirect(short_id):
    """Redirect to full URL by short link"""
    shortenerController = ShortenerController(r)
    return shortenerController.redirect(short_id)


@app.errorhandler(404)
def not_found(e):
    """Handler for 404 error"""
    return render_template('404.jinja'), 404
