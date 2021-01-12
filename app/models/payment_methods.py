from app.extensions import db


class PaymentMethod(db.Model):
    __tablename__ = "payment_methods"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True, unique=True)
    business_id = db.Column(db.Integer, db.ForeignKey("businesses.id"))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Category {self.name}"

    def to_dict(self):
        return {
            "name": self.name
        }
