from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Allergy(db.Model):
    __tablename__ = 'allergies'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    allergy_name = db.Column(db.String(100), nullable=False)

    def __init__(self, user_id, allergy_name):
        self.user_id = user_id
        self.allergy_name = allergy_name
