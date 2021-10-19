from .db import db

class Business(db.Model):
    __table__="businesses"

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    media_1 = db.Column(db.String, nullable=False)
    media_2 = db.Column(db.String)
    media_3 = db.Column(db.String)
    media_4 = db.Column(db.String)
    media_5 = db.Column(db.String)
    address = db.Column(db.String)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    zip_code = db.Column(db.String, nullable=False)

# many to one relationship with users
user = db.relationship('User', back_populates='businesses', lazy='subquery')
# one to many relationship with reviews
reviews = db.relationship('Review', back_populates='business', cascade="all, delete-orphan")
# many to one relationship with categories
category = db.relationship('Category', back_populates='businesses')


def to_dict(self):
    return {
        'id': self.id,
        'owner_id': self.owner_id,
        'category_id': self.category_id,
        'title': self.title,
        'description': self.description,
        'media_1': self.media_1,
        'media_2': self.media_2,
        'media_3': self.media_3,
        'media_4': self.media_4,
        'media_5': self.media_5,
        'address': self.address,
        'city': self.city,
        'state': self.state,
        'zip_code': self.zip_code,
        'category': self.category,
        'review': [review.to_dict() for review in self.reviews]
    }
