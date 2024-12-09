# Gerente Banco MVP

Este é um MVP (Minimum Viable Product) para um sistema de gerenciamento de clientes de um banco. O sistema permite que os gerentes de banco possam listar, pesquisar, editar e remover clientes, além de visualizar os produtos bancários que cada cliente está utilizando e o nível da conta (bronze, prata, ouro, diamante).

## Tecnologias Utilizadas

- **Python 3**
- **Flask**
- **SQLite**
- **Flask-SQLAlchemy**
- **Flask-Marshmallow**
- **Swagger UI**

## Estrutura do Projeto
gerente-banco-mvp/ ├── app.py ├── config.py ├── controllers/ │ └── cliente_controller.py ├── instance/ ├── models/ │ └── cliente.py ├── schemas/ │ └── cliente_schema.py ├── static/ │ └── swagger.json ├── venv/ ├── views/ │ └── cliente_view.py ├── README.md └── requirements.txt


## Configuração do Ambiente

1. **Clone o repositório:**

   ```sh
   git clone https://github.com/kevincoe/api-gerente-banco-mvp.git
   cd api-gerente-banco-mvp

2. Crie e ative o ambiente virtual:
    python3 -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`

3. Instale as dependências:
    pip3 install -r requirements.txt


## Executando a Aplicação:

1. Inicie a Aplicação:
    python3 app.py

2. Acesse a Aplicação:
    Abra o navegador e vá para http://127.0.0.1:5000/api

3. Documentação e Swagger:
    A documentação da API pode ser acessada e validada em http://127.0.0.1:5000/swagger


## Endpoints da API
    Clientes
    Listar todos os clientes:
    GET /api/clientes

    Obter um cliente pelo ID:
    GET /api/clientes/{id}

    Criar um novo cliente:
    POST /api/clientes
    Body:
        {
    "nome": "string",
    "agencia": "string",
    "conta": "string",
    "nivel": "string",
    "produtos": "string"
    }

    Atualizar um novo cliente:
    PATCH /api/clientes/{id}
    Body:
        {
    "nome": "string",
    "agencia": "string",
    "conta": "string",
    "nivel": "string",
    "produtos": "string"
    }

    Remover um cliente pelo ID:
    DELETE /api/clientes/{id}


##  Estrutura dos arquivos:
        app.py
        O arquivo principal que inicializa a aplicação Flask, configura o banco de dados e registra os blueprints.
        
        config.py
        Arquivo de configuração contendo as configurações do banco de dados.
        
        controllers/cliente_controller.py
        Contém a lógica de negócios para manipulação dos dados dos clientes.
        
        models/cliente.py
        Define o modelo Cliente usando SQLAlchemy.
        
        schemas/cliente_schema.py
        Define o schema ClienteSchema usando Marshmallow para serialização e desserialização dos dados.
        
        views/cliente_view.py
        Define as rotas da API para manipulação dos dados dos clientes.
        
        static/swagger.json
        Arquivo de configuração do Swagger para documentação da API.
        
        requirements.txt
        Lista de dependências do projeto.