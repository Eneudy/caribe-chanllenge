import click
from app.models import User
from app.extensions import db


def register(app):

    @app.cli.command()
    def deploy():
        """Run deployment tasks."""
        click.echo("Deploying app")

    @app.cli.command("create-db")
    def create_db():
        """Create database."""
        db.create_all()
        click.echo("Database created")

    @app.cli.command("create-user")
    @click.option("--name", default="admin", prompt="First name")
    @click.option("--email", default="admin@challenge.com", prompt="Email")
    @click.password_option()
    def create_admin(name, email, password):
        """Create user."""
        User.create_user(name=name, email=email, password=password)
        click.echo(f"User created")
