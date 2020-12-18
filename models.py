from app import db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    massage = db.Column(db.String(1000), nullable=False)

