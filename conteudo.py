from flask import Blueprint, jsonify
from models import Titulo
from app import db

content_bp = Blueprint('content_bp', __name__)

@content_bp.route('/titulos', methods=['GET'])
def listar_titulos():
    titulos = Titulo.query.all()
    titulos_data = [{'id': titulo.id, 'nome': titulo.nome} for titulo in titulos]
    return jsonify(titulos_data), 200
