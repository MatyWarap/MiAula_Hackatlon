from functools import wraps
from flask import session, redirect, url_for, flash

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Debes iniciar sesión.', 'warning')
            return redirect(url_for('users.user_login'))
        return f(*args, **kwargs)
    return decorated_function

def role_required(required_role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                flash('Debes iniciar sesión.', 'warning')
                return redirect(url_for('users.user_login'))

            if session.get('role') != required_role:
                flash('No tienes permisos para acceder a esta página.', 'danger')
                return redirect(url_for('users.user_login'))
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def logout_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id"):
            role = session.get("role")
            if role == "docente":
                flash("Ya has iniciado sesión.", "info")
                return redirect(url_for("users.dashboard_docente"))
            else:  # alumno
                flash("Ya has iniciado sesión.", "info")
                return redirect(url_for("users.dashboard_alumno"))
        return f(*args, **kwargs)
    return decorated_function