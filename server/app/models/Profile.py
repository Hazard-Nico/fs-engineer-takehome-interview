from app import db
from datetime import datetime

class Profile(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    identity_number = db.Column(db.String(16), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Constructor (__init__) accepting all fields
    def __init__(self, name, identity_number, email, date_of_birth):
        self.name = name
        self.identity_number = identity_number
        self.email = email
        self.date_of_birth = date_of_birth

    def __repr__(self):
        return "<Profile {}>".format(self.name)