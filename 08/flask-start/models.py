from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

VAT_MULTIPLIER = 1.23  # Stawka VAT 23%


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    is_available = db.Column(db.Boolean, default=True)

    def gross_price(self) -> float:
        return round(self.price * VAT_MULTIPLIER, 2)