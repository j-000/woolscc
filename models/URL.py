from server import db
import os
import datetime
import random
import string
from sqlalchemy import  (
    Table, 
    Column, 
    Integer, 
    String, 
    DateTime, 
    Boolean
)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
HOST = os.getenv('HOST')


class URL(Base):
    __tablename__ = 'urls'

    query = db.query_property()

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime(), default=datetime.datetime.utcnow)
    original_url = Column(String(200), nullable=False)
    follow_url = Column(String(200))
    identifier = Column(String(30))
    active = Column(Boolean(), default=True)
    
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

        db.add(self)
        db.commit()

    @staticmethod
    def _exists(url):
        found = URL.query.filter_by(original_url=url).first()
        return found
