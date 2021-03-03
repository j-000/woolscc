from server import db
import os
import datetime
import random
import string


HOST = os.getenv('HOST')


class URL(db.Model):
    __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    original_url = db.Column(db.String(200), nullable=False)
    follow_url = db.Column(db.String(200))
    identifier = db.Column(db.String(30))
    active = db.Column(db.Boolean(), default=True)
    
    def __init__(self, original_url, url_identifier_length=4):
        self.original_url = original_url

        # Identifiers need to start with B to ensure nginx can catch the request
        # and proxy it to the backend
        url_identifier = 'B'
        url_identifier += ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=url_identifier_length
            ))
        
        self.follow_url = f'{HOST}/{url_identifier}'
        self.identifier = url_identifier
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def _exists(url):
        found = URL.query.filter_by(original_url=url).first()
        return found
