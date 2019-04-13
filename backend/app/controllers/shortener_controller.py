import uuid

from flask import render_template, redirect, abort

from app.utilities.base64_converter import convert_base62

class ShortenerController:
    """The controller that handles requests to shortener service"""

    def __init__(self, redis):
        self.redis = redis

    def index(self):
        """Returns the index page"""
        return render_template('index.jinja')

    def post_url(self, url):
        """Posts new URL to shortener service"""
        url = url.strip()
        if (len(url) == 0):
            return self.index()

        id = uuid.uuid4()
        short_url_id = convert_base62(id.int)
        self.redis.set(short_url_id, url)

        return render_template('short_link.jinja', short_url = short_url_id)

    def redirect(self, short_id):
        """Redirects to URL by short link, or 404 otherwise"""
        url = self.redis.get(short_id.strip())
        if not url or len(url.strip()) == 0:
            abort(404) 

        return redirect(url)
