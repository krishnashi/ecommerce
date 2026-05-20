from flask import Blueprint, jsonify, request
from models.product_model import Product
from database.db import db
import json

product_bp = Blueprint("product_bp", __name__)

# GET ALL PRODUCTS
@product_bp.route("/products", methods=["GET"])
def get_products():

    products = Product.query.all()

    return jsonify([p.to_dict() for p in products])


# ADD PRODUCT
@product_bp.route("/products", methods=["POST"])
def add_product():

    data = request.json

    product = Product(
        name=data["name"],
        category=data["category"],
        price=data["price"],
        original_price=data.get("originalPrice"),
        rating=data.get("rating"),
        reviews=data.get("reviews"),
        badge=data.get("badge"),
        image=data.get("image"),
        colors=json.dumps(data.get("colors")),
        desc=data.get("desc")
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({
        "message": "Product added successfully"
    })