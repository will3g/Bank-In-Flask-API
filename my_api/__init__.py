from flask import Blueprint
from flask_restplus import Api

api = Blueprint('rest_api', __name__, url_prefix='/api')

rest_api = Api(version='1.0', title='Contas API', description='API de contas')
rest_api.init_app(api)

from my_api.resources.conta_resource import ns as conta_resource
rest_api.add_namespace(conta_resource, path='/contas')