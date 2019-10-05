from flask import request
from flask_restplus import Resource, Namespace, marshal_with
from my_api.models.conta import Conta
from my_api.utils.serializers import conta_input_dto, conta_output_dto
from database import db

ns = Namespace('contas', description='operações das contas')

@ns.route('/')
class ContasResource(Resource):

    @marshal_with(conta_output_dto)
    def get(self):
        return Conta.query.all()

    @marshal_with(conta_output_dto)
    @ns.expect(conta_input_dto)
    def post(self):
        data = request.get_json()
        numero = data.get('numero')
        titular = data.get('titular')
        saldo = float(data.get('limite'))
        limite = float(data.get('limite'))

        conta = Conta(numero, titular, saldo, limite)

        db.session.add(conta)
        db.session.commit()
        return conta