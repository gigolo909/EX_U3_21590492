from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models.contacto import Contacto

# Definición del Blueprint
# IMPORTANTE: El primer nombre 'contacto' es clave para que funcionen los enlaces.
contacto_bp = Blueprint('contacto', __name__, url_prefix='/contactos')

# --------------------------------------------------------------------------
# RUTAS DE LECTURA (GET)
# --------------------------------------------------------------------------

# 1. LISTADO (Se accede en /contactos/)
@contacto_bp.route('/')
def listar_contactos():
    contactos = Contacto.query.all()
    # Asegúrate de que tu archivo HTML se llame 'listado.html' o cambia el nombre aquí
    return render_template('listado.html', contactos=contactos)

# 2. FORMULARIO NUEVO (Se accede en /contactos/nuevo)
@contacto_bp.route('/nuevo')
def nuevo_contacto():
    return render_template('crear.html')

# 3. FORMULARIO EDITAR (Se accede en /contactos/editar/ID)
@contacto_bp.route('/editar/<int:id>')
def editar_contacto(id):
    contacto = Contacto.query.get_or_404(id)
    return render_template('editar.html', contacto=contacto)

# --------------------------------------------------------------------------
# RUTAS DE ACCIÓN (POST y ELIMINAR)
# --------------------------------------------------------------------------

# 4. GUARDAR (Recibe datos del formulario de crear)
@contacto_bp.route('/guardar', methods=['POST'])
def guardar_contacto():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    correo = request.form['correo']  # ¡No olvides que el input en HTML debe tener name="correo"!

    nuevo = Contacto(nombre=nombre, telefono=telefono, correo=correo)
    
    db.session.add(nuevo)
    db.session.commit()

    return redirect(url_for('contacto.listar_contactos'))

# 5. ACTUALIZAR (Recibe datos del formulario de editar)
@contacto_bp.route('/actualizar/<int:id>', methods=['POST'])
def actualizar_contacto(id):
    contacto = Contacto.query.get_or_404(id)
    
    contacto.nombre = request.form['nombre']
    contacto.telefono = request.form['telefono']
    contacto.correo = request.form['correo']

    db.session.commit()
    return redirect(url_for('contacto.listar_contactos'))

# 6. ELIMINAR (Borra el contacto y regresa a la lista)
@contacto_bp.route('/eliminar/<int:id>')
def eliminar_contacto(id):
    contacto = Contacto.query.get_or_404(id)
    db.session.delete(contacto)
    db.session.commit()
    return redirect(url_for('contacto.listar_contactos'))