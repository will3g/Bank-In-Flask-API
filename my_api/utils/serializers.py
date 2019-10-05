from flask_restplus import fields
from my_api import rest_api

conta_output_dto = rest_api.model('conta', {
    'id': fields.Integer,
    'numero': fields.String,
    'titular': fields.String,
    'saldo': fields.Float,
    'limite': fields.Float
})

conta_input_dto = rest_api.model('conta', {
    'numero': fields.String,
    'titular': fields.String,
    'saldo': fields.Float,
    'limite': fields.Float
})