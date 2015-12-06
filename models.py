import mongoengine as me
from datetime import datetime
from config import DATABASE_NAME


# Connect to the Mongo database
me.connect(DATABASE_NAME)


class Page(me.Document):
    """Represents a page."""
    title = me.StringField(required=True)
    author = me.StringField(required=True)
    body = me.StringField()
    created_at = me.DateTimeField(default=datetime.now)


class Profile(me.Document):
    """Represents a Github user profile."""
    raw_json = me.DynamicField()
    downloaded_at = me.DateTimeField(default=datetime.now)
