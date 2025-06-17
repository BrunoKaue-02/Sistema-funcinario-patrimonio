from flask import request, jsonify
from app.models import Funcionario
from app.database.db import db

def listar_todos():
    funcionarios = Funcionario.query.all()
    return jsonify([f.to_dict() for f in funcionarios]), 200

