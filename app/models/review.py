from .db import db


class Review(db.Model):
    __tablename__='reviews'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String, nullable=False)
    media_1 = db.Column(db.String)
    media_2 = db.Column(db.String)
    media_3 = db.Column(db.String)
    media_4 = db.Column(db.String)
    media_5 = db.Column(db.String)

# many to one relationship with businesses
business = db.relationship('Business', back_populates='reviews')
# many to one relationship with user
user = db.relationship('User', back_populates='reviews')


def to_dict(self):
    return {
        'id': self.id,
        'user_id': self.user_id,
        'business_id': self.business_id,
        'rating': self.rating,
        'content': self.content,
        'media_1': self.media_1,
        'media_2': self.media_2,
        'media_3': self.media_3,
        'media_4': self.media_4,
        'media_5': self.media_5,
        'business': self.business,
        'user': self.user
    }
