from flask import Blueprint, request, jsonify
from controllers.cliente_controller import ClienteController
from schemas.cliente_schema import ClienteSchema

cliente_bp = Blueprint('cliente_bp', __name__)
cliente_schema = ClienteSchema()
clientes_schema = ClienteSchema(many=True)

@cliente_bp.route('/clientes', methods=['GET'])
def listar_clientes():
    clientes = ClienteController.listar_clientes()
    return clientes_schema.jsonify(clientes)

@cliente_bp.route('/clientes/<int:id>', methods=['GET'])
def obter_cliente(id):
    cliente = ClienteController.obter_cliente(id)
    return cliente_schema.jsonify(cliente)

@cliente_bp.route('/clientes', methods=['POST'])
def criar_cliente():
    data = request.get_json()
    novo_cliente = ClienteController.criar_cliente(data)
    return cliente_schema.jsonify(novo_cliente), 201

@cliente_bp.route('/clientes/<int:id>', methods=['PUT'])
def atualizar_cliente(id):
    data = request.get_json()
    cliente = ClienteController.atualizar_cliente(id, data)
    return cliente_schema.jsonify(cliente)

@cliente_bp.route('/clientes/<int:id>', methods=['DELETE'])
def remover_cliente(id):
    cliente = ClienteController.remover_cliente(id)
    return cliente_schema.jsonify(cliente)