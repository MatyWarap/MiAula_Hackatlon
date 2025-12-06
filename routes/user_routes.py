from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from config.db import db
from models.user import User
from models.result import Resultado
from utils.authentication import login_required, role_required, logout_required

users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
@logout_required
def user_register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        role = request.form.get('role', 'alumno')

        if password.lower() == name.lower():
            flash("La contraseña no puede ser igual al nombre de usuario.", "danger")
            return redirect(url_for('users.user_register'))

        existing_user = User.query.filter_by(name=name).first()
        if existing_user:
            flash("Ese nombre de usuario ya existe.", "danger")
            return redirect(url_for('users.user_register'))

        new_user = User(name=name, password=password, role=role)
        db.session.add(new_user)
        db.session.commit()

        flash("Usuario registrado correctamente.", "success")
        return redirect(url_for('users.user_login'))

    return render_template('users/register.html')

@users.route('/login', methods=['GET', 'POST'])
@logout_required
def user_login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        user = User.query.filter_by(name=name).first()

        if user and user.check_password(password):
            session['user_id'] = user.id_user
            session['role'] = user.role
            session['name'] = user.name

            flash("Bienvenido " + user.name, "success")

            # redirigir según rol
            if user.role == 'docente':
                return redirect(url_for('users.dashboard_docente'))
            else:
                return redirect(url_for('users.materias'))

        flash("Credenciales incorrectas.", "danger")
        return redirect(url_for('users.user_login'))

    return render_template('users/login.html')

@users.route("/logout")
@login_required
def logout():
    session.clear()  # Borra toda la sesión
    flash("Has cerrado sesión correctamente.", "success")
    return redirect(url_for("home"))

# @users.route('/dashboard/alumno')
# @login_required
# @role_required('alumno')
# def dashboard_alumno():
#     return render_template('users/dashboard_alumno.html')

@users.route('/dashboard/docente')
@login_required
@role_required('docente')
def dashboard_docente():
    return render_template('users/dashboard_docente.html')

@users.route('/alumno/materias')
@login_required
@role_required('alumno')
def materias():
    materias = [
        ("Lengua", "📘", "bg-danger"),
        ("Matemática", "🔢", "bg-primary"),
        ("Ciencias Naturales", "🧪", "bg-success"),
        ("Ciencias Sociales", "🌍", "bg-warning")
    ]
    return render_template("users/materias.html", materias=materias)

@users.route('/alumno/trivia/<materia>', methods=['GET', 'POST'])
@login_required
@role_required('alumno')
def trivia(materia):
    from utils.preguntas_data import preguntas_por_materia
    
    preguntas = preguntas_por_materia.get(materia, [])

    if request.method == "POST":
        puntaje = 0
        for p in preguntas:
            respuesta = request.form.get(str(p["id"]))
            if respuesta == p["respuesta"]:
                puntaje += 1

        nuevo = Resultado(
            id_user=session.get("user_id"),
            materia=materia,
            puntaje=puntaje,
            total=len(preguntas)
        )

        db.session.add(nuevo)
        db.session.commit()

        return render_template(
            "users/resultado.html",
            puntaje=puntaje,
            total=len(preguntas),
            materia=materia
        )

    return render_template(
        "users/trivia.html",
        materia=materia,
        preguntas=preguntas
    )

    

@users.route('/dashboard/docente/resultados')
@login_required
@role_required('docente')
def resultados_docente():
    from models.user import User
    from models.result import Resultado

    alumnos = User.query.filter_by(role="alumno").all()
    materia_filtro = request.args.get("materia", "")
    alumno_filtro = request.args.get("alumno", "")

    query = Resultado.query.join(User)

    if alumno_filtro:
        query = query.filter(Resultado.id_user == alumno_filtro)

    if materia_filtro:
        query = query.filter(Resultado.materia == materia_filtro)

    resultados = query.order_by(Resultado.fecha.desc()).all()

    materias = ["Lengua", "Matemática", "Ciencias Naturales", "Ciencias Sociales"]

    return render_template(
        "users/resultados_docente.html",
        resultados=resultados,
        alumnos=alumnos,
        materias=materias,
        alumno_filtro=alumno_filtro,
        materia_filtro=materia_filtro
    )



#--------------------------------

@users.route('/docente/preguntas')
@login_required
@role_required('docente')
def listar_preguntas():
    from models.pregunta import Pregunta

    preguntas = Pregunta.query.all()

    return render_template(
        'users/preguntas_listar.html',
        preguntas=preguntas
    )


@users.route('/docente/preguntas/nueva', methods=['GET', 'POST'])
@login_required
@role_required('docente')
def nueva_pregunta():
    from models.pregunta import Pregunta

    materias = ["Lengua", "Matemática", "Ciencias Naturales", "Ciencias Sociales"]

    if request.method == 'POST':

        nueva = Pregunta(
            materia=request.form['materia'],
            pregunta=request.form['pregunta'],
            opcion1=request.form['op1'],
            opcion2=request.form['op2'],
            opcion3=request.form['op3'],
            respuesta_correcta=request.form['correcta']
        )

        db.session.add(nueva)
        db.session.commit()

        flash("Pregunta creada correctamente.", "success")
        return redirect(url_for('users.listar_preguntas'))

    return render_template(
        'users/preguntas_nueva.html',
        materias=materias
    )


@users.route('/docente/preguntas/editar/<id>', methods=['GET', 'POST'])
@login_required
@role_required('docente')
def editar_pregunta(id):
    from models.pregunta import Pregunta

    pregunta = Pregunta.query.get(id)
    materias = ["Lengua", "Matemática", "Ciencias Naturales", "Ciencias Sociales"]

    if request.method == 'POST':
        pregunta.materia = request.form['materia']
        pregunta.pregunta = request.form['pregunta']
        pregunta.opcion1 = request.form['op1']
        pregunta.opcion2 = request.form['op2']
        pregunta.opcion3 = request.form['op3']
        pregunta.respuesta_correcta = request.form['correcta']

        db.session.commit()

        flash("Pregunta actualizada.", "success")
        return redirect(url_for('users.listar_preguntas'))

    return render_template(
        'users/preguntas_editar.html',
        pregunta=pregunta,
        materias=materias
    )


@users.route('/docente/preguntas/eliminar/<id>')
@login_required
@role_required('docente')
def eliminar_pregunta(id):
    from models.pregunta import Pregunta

    pregunta = Pregunta.query.get(id)

    db.session.delete(pregunta)
    db.session.commit()

    flash("Pregunta eliminada.", "success")

    return redirect(url_for('users.listar_preguntas'))
