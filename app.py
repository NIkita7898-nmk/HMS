from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

with app.app_context():
    app.config['SQLALCHEMY_DATABASE_URI'] = f'{os.environ.get("DB_ENGINE")}://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASSWORD")}@{os.environ.get("DB_HOST")}:{os.environ.get("DB_PORT")}/{os.environ.get("DB_NAME")}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Suppresses a warning
    if "sqlalchemy" not in app.extensions:
        db = SQLAlchemy()
        db.init_app(app)
        print(app.extensions, "++++++++++++++++++++++++")
    migrate = Migrate(app, db)

    if __name__ == '__main__':
        from api.route import routes
        app.register_blueprint(routes)
        app.run(debug=True)
        db.create_all()
        db.session.commit()
