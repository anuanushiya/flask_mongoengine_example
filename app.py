from flask import Flask, render_template
from models import Page

app = Flask(__name__)


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

