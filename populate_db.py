"""Run this script once to populate your database with some sample data."""

import mongoengine as me
from models import Page
from datetime import datetime
from faker import Factory
from config import DATABASE_NAME


def create_pages(quantity):
    """Creates pages and saves them in the database."""
    # Connect to database
    me.connect(DATABASE_NAME)

    # Instantiate a fake data factory
    fake = Factory.create()

    for page in range(1, quantity+1):
        # Instantiate a new Page object (from models.py)
        current_page = Page()

        # Add fake data to the fields
        current_page['title'] = ' '.join(fake.words()).capitalize()
        current_page['author'] = fake.name()
        current_page['body'] = fake.text()
        print('Saving a new page: {} by {}'.format(current_page['title'],
                                                   current_page['author']))

        # Save the page
        current_page.save()


if __name__ == '__main__':
    create_pages(10)
