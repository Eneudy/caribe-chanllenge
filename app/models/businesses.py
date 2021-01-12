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

    # Helper methods
    def get_tags(self):
        return [tag.name for tag in self.tags.all()]

    def get_payment_methods(self):
        return [{"id": pm.id, "name": pm.name} for pm in self.payment_methods.all()]

    def get_categories(self):
        return [{"id": ct.id, "name": ct.name} for ct in self.categories.all()]

    def get_schedules(self):
        return [{"id": sc.id, "day": sc.day, "open": sc.open, "close": sc.close} for sc in self.schedules.all()]

    def get_languages(self):
        return [{"id": lg.id, "language": lg.language} for lg in self.languages.all()]

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "address": self.address,
            "phone": self.phone,
            "website": self.website,
            "logo": self.logo,
            "tags": self.get_tags(),
            "city": self.cities.first().name,
            "country": self.cities.first().country,
            "zip_code": self.cities.first().zip_code,
            "categories": self.get_categories(),
            "schedules": self.get_schedules(),
            "languages": self.get_languages(),
        }
