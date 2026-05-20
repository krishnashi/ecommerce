from flask import Flask
from flask_cors import CORS
from config import Config
from database.db import db
from routes.product_routes import product_bp

app = Flask(__name__)


app.register_blueprint(product_bp)

app.config.from_object(Config)

CORS(app)

db.init_app(app)

@app.route("/")
def home():
    return {"message": "Backend running"}

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)