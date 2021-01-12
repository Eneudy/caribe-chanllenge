from app.extensions import db


class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True, unique=True)
    points = db.Column(db.Integer)
    business_id = db.Column(db.Integer, db.ForeignKey("businesses.id"))

    def __init__(self, name, points):
        self.name = name
        self.points = points

    def __repr__(self):
        return f"Category {self.name}"

    def to_dict(self):
        return {
            "name": self.name,
            "points": self.points
        }
