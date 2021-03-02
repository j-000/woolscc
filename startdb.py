from server import db
from models.URL import URL


db.drop_all()
db.create_all()