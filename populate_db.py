"""Run this script once to populate your database with some sample data."""

import mongoengine as me
from models import Page
from datetime import datetime

me.connect('database_name')

page1 = Page(title='Saluton, Mondo!', body='This is the body.')
page2 = Page(title='This is another page', body='Some body text for page #2.')

page1.save()
page2.save()
