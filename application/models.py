from application import db


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True,serial=True)
    isbn = db.Column(db.String(30), unique=True, nullable=False)
    title = db.Column(db.String(200), unique=True, nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer(4), nullable=False)
    