from database.db import db
import json

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(200), nullable=False)

    category = db.Column(db.String(100), nullable=False)

    price = db.Column(db.Float, nullable=False)

    original_price = db.Column(db.Float)

    rating = db.Column(db.Float)

    reviews = db.Column(db.Integer)

    badge = db.Column(db.String(50))

    image = db.Column(db.String(50))

    colors = db.Column(db.Text)

    desc = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "originalPrice": self.original_price,
            "rating": self.rating,
            "reviews": self.reviews,
            "badge": self.badge,
            "image": self.image,
            "colors": json.loads(self.colors),
            "desc": self.desc
        }