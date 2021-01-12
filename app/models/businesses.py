from app.extensions import db


class Business(db.Model):
    __tablename__ = "businesses"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True, nullable=False)
    description = db.Column(db.String(200))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(100))
    website = db.Column(db.String(100))
    logo = db.Column(db.String(100))

    # Relationships
    categories = db.relationship("Category", cascade="all,delete",
                                 backref="business", lazy="dynamic")
    
    cities = db.relationship("City", cascade="all,delete",
                             backref="business", lazy="dynamic")
    
    languages = db.relationship("Language", cascade="all,delete",
                                backref="business", lazy="dynamic")
    
    payment_methods = db.relationship("PaymentMethod", cascade="all,delete",
                                      backref="business", lazy="dynamic")
    
    schedules = db.relationship("Schedule", cascade="all,delete",
                                 backref="business", lazy="dynamic")
    
    tags = db.relationship("Tag", cascade="all,delete",
                            backref="business", lazy="dynamic")

    def __init__(self, name, description, address, phone, website, logo):
        self.name = name
        self.description = description
        self.address = address
        self.phone = phone
        self.website = website
        self.logo = logo

    def __repr__(self):
        return f"Business {self.name}"

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "address": self.address,
            "phone": self.phone,
            "website": self.website,
            "logo": self.logo
        }
