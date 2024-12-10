from flask import Flask
from flask_cors import CORS
from config import Config
from models.cliente import db
from schemas.cliente_schema import ma
from views.cliente_view import cliente_bp
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

db.init_app(app)
ma.init_app(app)

app.register_blueprint(cliente_bp, url_prefix='/api')

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Gerente Banco API"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)