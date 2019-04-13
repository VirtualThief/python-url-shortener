from flask import render_template

class ShortenerController:
    """The controller that handles requests to shortener service"""

    def index(self):
        """Returns the index page"""
        return render_template('index.jinja')

    def postUrl(self, url):
        """Posts new URL to shortener service"""
        url = url.strip()
        if (len(url) == 0):
            return self.index()

        return url