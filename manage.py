from app import create_app, cli
from app.extensions import db
from app.models import User, Business

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Business": Business}
