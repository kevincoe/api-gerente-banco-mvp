from models.cliente import db, Cliente
from models.investimento import Investimento
from services.finance_service import FinanceService
from datetime import datetime

class InvestimentoController:
    @staticmethod
    def listar_investimentos(cliente_id):
        """Lista todos os investimentos de um cliente"""
        return Investimento.query.filter_by(cliente_id=cliente_id).all()
    
    @staticmethod
    def obter_investimento(id):
        """Obtém um investimento específico pelo ID"""
        return Investimento.query.get_or_404(id)
    
    @staticmethod
    def comprar_acao(cliente_id, data):
        """Compra ações para um cliente"""
        cliente = Cliente.query.get_or_404(cliente_id)
        simbolo = data['simbolo']
        quantidade = float(data['quantidade'])
        
        # Verificar quantidade válida
        if quantidade <= 0:
            return {"erro": "A quantidade deve ser um valor positivo"}, 400
        
        # Obter preço atual da ação
        preco_atual = FinanceService.get_stock_price(simbolo)
        if preco_atual is None:
            return {"erro": f"Não foi possível obter o preço para a ação {simbolo}"}, 400
        
        # Calcular valor total da compra
        valor_total = preco_atual * quantidade
        
        # Verificar saldo suficiente
        if cliente.saldo < valor_total:
            return {"erro": f"Saldo insuficiente. Necessário: R$ {valor_total:.2f}, Disponível: R$ {cliente.saldo:.2f}"}, 400
        
        # Criar o investimento
        investimento = Investimento(
            cliente_id=cliente_id,
            tipo="acao",
            simbolo=simbolo,
            quantidade=quantidade,
            preco_compra=preco_atual
        )
        
        # Atualizar saldo do cliente
        cliente.saldo -= valor_total
        
        # Persistir no banco
        db.session.add(investimento)
        db.session.commit()
        
        return investimento, 201
    
    @staticmethod
    def comprar_dolar(cliente_id, data):
        """Compra dólares para um cliente"""
        cliente = Cliente.query.get_or_404(cliente_id)
        quantidade = float(data['quantidade'])
        
        # Verificar quantidade válida
        if quantidade <= 0:
            return {"erro": "A quantidade deve ser um valor positivo"}, 400
        
        # Obter cotação atual do dólar
        cotacao_atual = FinanceService.get_currency_price()
        if cotacao_atual is None:
            return {"erro": "Não foi possível obter a cotação do dólar"}, 400
        
        # Calcular valor total em reais
        valor_total = cotacao_atual * quantidade
        
        # Verificar saldo suficiente
        if cliente.saldo < valor_total:
            return {"erro": f"Saldo insuficiente. Necessário: R$ {valor_total:.2f}, Disponível: R$ {cliente.saldo:.2f}"}, 400
        
        # Criar o investimento
        investimento = Investimento(
            cliente_id=cliente_id,
            tipo="moeda",
            simbolo="USD",
            quantidade=quantidade,
            preco_compra=cotacao_atual
        )
        
        # Atualizar saldo do cliente
        cliente.saldo -= valor_total
        
        # Persistir no banco
        db.session.add(investimento)
        db.session.commit()
        
        return investimento, 201
    
    @staticmethod
    def calcular_valor_carteira(cliente_id):
        """Calcula o valor atual da carteira de investimentos do cliente"""
        investimentos = Investimento.query.filter_by(cliente_id=cliente_id).all()
        valor_atual = FinanceService.get_portfolio_value(investimentos)
        return {"cliente_id": cliente_id, "valor_carteira": valor_atual}