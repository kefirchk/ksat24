from flask import Flask
from app.config import config
from app.database import db
from app.services import InputService


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Регистрация обработчиков
    from app.views import main_bp
    app.register_blueprint(main_bp)

    return app
