from flask import Blueprint, request, jsonify
from models import Usuario
from app import db

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/cadastro', methods=['POST'])
def cadastro():
    data = request.get_json()
    usuario = Usuario(username=data['username'], email=data['email'])
    usuario.set_password(data['senha'])
    db.session.add(usuario)
    db.session.commit()
    return jsonify({'mensagem': 'Usuário cadastrado com sucesso!'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    # Implemente a lógica de login usando JWT
    pass
