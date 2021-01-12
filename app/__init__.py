from flask import Flask, jsonify
from config import Config
from app.extensions import db, jtw

# Register models with sqlalchemy
from app import models


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    # Init extensions
    db.init_app(app)
    jtw.init_app(app)
    # Registers
    register_blueprints(app)
    register_error_handlers(app)
    return app


def register_blueprints(app):
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix="/api")


def register_error_handlers(app):

    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({"error": "Bad request"}), 400

    @app.errorhandler(404)
    def resource_not_found(e):
        return jsonify({"error": "Resource not found"}), 404

    @app.errorhandler(405)
    def method_not_allowed(e):
        return jsonify({"error": "Method not allowed"}), 405

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({"error": "Server error"}), 500
