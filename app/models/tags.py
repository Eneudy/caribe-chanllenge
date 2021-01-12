from app.extensions import db


class Tag(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True, unique=True)
    business_id = db.Column(db.Integer, db.ForeignKey("businesses.id"))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Tag {self.name}"

    def to_dict(self):
        return {
            "name": self.name
        }
