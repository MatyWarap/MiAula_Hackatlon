from flask import Flask, render_template, redirect, url_for, session
from config.db import db
from config.config import Config
from routes.user_routes import users

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(users)

@app.route("/")
def home():
    # Si el usuario ya inició sesión, redirigir según rol
    if session.get("user_id"):
        role = session.get("role")
        if role == "docente":
            return redirect(url_for("users.dashboard_docente"))
        else:  # alumno
            return redirect(url_for("users.materias"))

    # Si no hay sesión, mostrar la página de inicio
    return render_template("home.html")

if __name__ == "__main__":
    with app.app_context():
        from models.user import User
        from models.result import Resultado
        from models.pregunta import Pregunta
        db.create_all()
    app.run(debug=True)