from app.extensions import db


class Business(db.model):
    __tablename__ = "business"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True)
    description = db.Column(db.String(200))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(100))
    website = db.Column(db.String(100))

    """
    Relationships:
    - City (id, name, country, zip_code)
    - Tag (id, name)
    - Category (id, name, points)
    - PaymentMethod (id, name)
    - Schedule (id, day, open, close)
    - Language (id, language)
    """
