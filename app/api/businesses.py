from flask import jsonify, request
from flask_jwt_extended import jwt_required
from app.extensions import db
from app.models import Business

from . import bp


@bp.route("/businesses")
@jwt_required
def get_businesses():
    # /?term=Some test
    # /?sort_by=city&order_by=desc
    # /?city=Santo Domingo
    businesses = Business.query.all()
    rv = [business.to_dict() for business in businesses]
    return jsonify(rv)
