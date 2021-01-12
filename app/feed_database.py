from app.extensions import db
from app.models import (Business, Category, City, Language, 
                        PaymentMethod, Schedule, Tag)
from flask import current_app


def insert_data():

    with current_app.app_context():

        # Business 1
        business_1 = Business(name="Consolidated Moving & Storage SRL", 
                            description="39 Years of Professional Moving Services",
                            address="542 Mount Pleasant Santo Domingo",
                            phone="+1 (809) 654-0983",
                            website="https://www.consolidatedmoving.com.do",
                            logo="https://picsum.photos/200/300")

        city_1 = City(name="Santo Domingo", country="Dominican Republic", zip_code=10123)
        city_1.business = business_1

        tag_1 = Tag(name="services")
        tag_2 = Tag(name="storage")
        tag_1.business = business_1
        tag_2.business = business_1

        category_1 = Category(name="Movements", points=2)
        category_1.business = business_1

        payment_1 = PaymentMethod(name="Visa")
        payment_2 = PaymentMethod(name="Mastercard")
        payment_1.business = business_1
        payment_2.business = business_1

        schedule_1 = Schedule(day=1, open="7:00", close="18:00")
        schedule_2 = Schedule(day=2, open="7:00", close="18:00")
        schedule_3 = Schedule(day=3, open="7:00", close="18:00")
        schedule_1.business = business_1
        schedule_2.business = business_1
        schedule_3.business = business_1

        language_1 = Language(language="Spanish")
        language_1.business = business_1

        db.session.add(business_1)
        db.session.commit()
