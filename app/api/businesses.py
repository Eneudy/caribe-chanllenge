from flask import jsonify, request
from flask_jwt_extended import jwt_required
from app.extensions import db
from app.models import Business

from . import bp


@bp.route("/businesses")
def get_businesses():
    businesses = Business.query.all()
    rv = [business.to_dict() for business in businesses]
    return jsonify(rv)
