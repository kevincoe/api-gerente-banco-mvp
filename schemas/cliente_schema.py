from flask_marshmallow import Marshmallow
from models.cliente import Cliente

ma = Marshmallow()

class ClienteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cliente