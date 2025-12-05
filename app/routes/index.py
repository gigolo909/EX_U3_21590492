from flask import Blueprint, render_template
from app.models.contacto import Contacto

index_bp = Blueprint('index_bp', __name__)

@index_bp.route('/')
def index():
    contactos = Contacto.query.all()
    return render_template('index.html', contactos=contactos)
