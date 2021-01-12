from app.extensions import db


class Language(db.Model):
    __tablename__ = "languages"
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(60), index=True, unique=True)
    business_id = db.Column(db.Integer, db.ForeignKey("businesses.id"))

    def __init__(self, language):
        self.language = language

    def __repr__(self):
        return f"Language {self.language}"

    def to_dict(self):
        return {
            "language": self.language
        }
