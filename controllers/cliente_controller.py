from models.cliente import db, Cliente

class ClienteController:
    @staticmethod
    def listar_clientes():
        return Cliente.query.all()

    @staticmethod
    def obter_cliente(id):
        return Cliente.query.get_or_404(id)

    @staticmethod
    def criar_cliente(data):
        novo_cliente = Cliente(
            nome=data['nome'],
            agencia=data['agencia'],
            conta=data['conta'],
            nivel=data['nivel'],
            produtos=data.get('produtos', '')
        )
        db.session.add(novo_cliente)
        db.session.commit()
        return novo_cliente

    @staticmethod
    def atualizar_cliente(id, data):
        cliente = Cliente.query.get_or_404(id)
        if 'nome' in data:
            cliente.nome = data['nome']
        if 'agencia' in data:
            cliente.agencia = data['agencia']
        if 'conta' in data:
            cliente.conta = data['conta']
        if 'nivel' in data:
            cliente.nivel = data['nivel']
        if 'produtos' in data:
            cliente.produtos = data['produtos']
        db.session.commit()
        return cliente

    @staticmethod
    def remover_cliente(id):
        cliente = Cliente.query.get_or_404(id)
        db.session.delete(cliente)
        db.session.commit()
        return cliente