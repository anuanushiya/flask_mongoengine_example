import mongoengine as me
from datetime import datetime


me.connect('database_name')

class Page(me.Document):
    """Represents a page."""
    title = me.StringField(required=True)
    body = me.StringField()
    created_at = me.DateTimeField(default=datetime.now())
