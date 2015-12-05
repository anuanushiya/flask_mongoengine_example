from flask import Flask, render_template
import mongoengine as me
from datetime import datetime


app = Flask(__name__)

me.connect('database_name')

# This could go in models.py
class Page(me.Document):
    title = me.StringField(required=True)
    body = me.StringField()
    created_at = me.DateTimeField(default=datetime.now())


@app.route('/')
def index():
    """Gets all pages from the database."""
    pages = Page.objects
    return render_template('index.html', pages=pages)


@app.route('/page/<page_id>/')
def page(page_id):
    """Gets one page from the database."""
    page = Page.objects.get(id=page_id)
    return render_template('page.html', page=page)


if __name__ == '__main__':
    app.run(debug=True)

