from app.extensions import db


class Schedule(db.Model):
    __tablename__ = "schedules"
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Integer)
    open = db.Column(db.String(60))
    close = db.Column(db.String(60))
    business_id = db.Column(db.Integer, db.ForeignKey("businesses.id"))

    def __init__(self, day, open, close):
        self.day = day
        self.open = open
        self.close = close

    def __repr__(self):
        return f"Schedule {self.day}, Open {self.open},  Close {self.close}"

    def to_dict(self):
        return {
            "day": self.day,
            "open": self.open,
            "close": self.close
        }
