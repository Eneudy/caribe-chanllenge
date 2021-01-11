from flask import jsonify, request
from flask_jwt_extended import jwt_required
from app.extensions import db
from app.models import User

from .errors import bad_request
from . import bp


@bp.route("/users")
def get_users():
    users = User.query.all()
    rv = [user.to_dict() for user in users]
    return jsonify(rv)


@bp.route("/users", methods=["POST"])
@jwt_required
def create_user():
    data = request.get_json(force=True) or {}
    if not data.get("name") or not data.get("email") or not data.get("password"):
        return bad_request("Required name, email and password")
    if User.query.filter_by(email=data.get("email")).first():
        return bad_request("Email already in database")
    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"user": new_user.to_dict()})
