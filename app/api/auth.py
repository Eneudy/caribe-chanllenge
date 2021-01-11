from flask import jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from datetime import timedelta
from app.extensions import db
from app.models import User

from .errors import error_response
from . import bp


@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(force=True)
    user = User.query.filter_by(email=data.get("email", "")).first()
    if user and user.check_password(data.get("password", "")):
        expires = timedelta(days=1)
        access_token = create_access_token(identity=user.name, expires_delta=expires)
        return jsonify({"token": access_token})
    return error_response(status_code=401, message="Invalid data")


@bp.route("/protected")
@jwt_required
def protected():
    user = get_jwt_identity()
    print(user)
    return jsonify({"ok": True})
