from config.db import db
import uuid

class Pregunta(db.Model):
    __tablename__ = "preguntas"

    id_pregunta = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    materia = db.Column(db.String(50), nullable=False)
    pregunta = db.Column(db.String(255), nullable=False)

    opcion1 = db.Column(db.String(255), nullable=False)
    opcion2 = db.Column(db.String(255), nullable=False)
    opcion3 = db.Column(db.String(255), nullable=False)

    respuesta_correcta = db.Column(db.String(255), nullable=False)