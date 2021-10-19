from .db import db


class Category(db.Mode):
    __tablename__="categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.String(db.String, nullable=False)


# one to many relationship with businesses
businesses = db.relationship('Business', back_populates='category')
