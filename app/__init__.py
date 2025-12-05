from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contactos.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)

    from app.routes.index import index_bp
    from app.routes.contacto import contacto_bp

    app.register_blueprint(index_bp)
    app.register_blueprint(contacto_bp)

    # 👉 CREA LAS TABLAS AUTOMÁTICAMENTE
    with app.app_context():
        db.create_all()

    return app
