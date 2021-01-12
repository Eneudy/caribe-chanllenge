from app.extensions import db


class City(db.Model):
    __tablename__ = "cities"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True, unique=True)
    country = db.Column(db.String(60), index=True)
    zip_code = db.Column(db.Integer)
    business_id = db.Column(db.Integer, db.ForeignKey("businesses.id"))

    def __init__(self, name, country, zip_code):
        self.name = name
        self.country = country
        self.zip_code = zip_code

    def __repr__(self):
        return f"City {self.name}"

    def to_dict(self):
        return {
            "name": self.name,
            "country": self.country,
            "zip_code": self.zip_code
        }
