from config.db import db
import uuid
from datetime import datetime

class Resultado(db.Model):
    __tablename__ = "resultados"

    id_resultado = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    id_user = db.Column(db.String(36), db.ForeignKey("users.id_user"), nullable=False)

    materia = db.Column(db.String(50), nullable=False)
    puntaje = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)

    fecha = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", backref="resultados")