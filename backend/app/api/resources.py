"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

import json
from datetime import datetime
from flask import request
from flask_restplus import Resource

from .security import require_auth
from .SmartCheck import SmartCheck
from . import api_rest

# load configs from config.json
contracts_settings = './contracts_settings.json'

with open(contracts_settings, 'r') as f:
    keys = ['contractList','network','tx_hash']
    configs = json.load(f)
    kwargs = { key: configs[key] for key in keys }

class SecureResource(Resource):
    """ Calls require_auth decorator on all requests """
    method_decorators = [require_auth]


@api_rest.route('/resource/<string:resource_id>')
class ResourceOne(Resource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}

    def post(self, resource_id):
        json_payload = request.json
        return {'timestamp': json_payload}, 201


@api_rest.route('/secure-resource/<string:resource_id>')
class SecureResourceOne(SecureResource):
    """ Secure Resource Class: Inherit from Resource """

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}

@api_rest.route('/contracts/<string:resource_id>')
class SecureSmartContract(Resource):
    """ Secure Resource Class: Inherit from Resource """

    def get(self, resource_id):
        module = SmartCheck(**kwargs)
        return {
            'createStudent': lambda: self.createStudent(module),
            'getParticularStudent': lambda: self.getParticularStudent(module),
            'getStudents': lambda: self.getStudents(module)
        }.get(resource_id, lambda: None)()

    def createStudent(self, module):
        studId = request.args.get('studId')
        age = request.args.get('age')
        fName = request.args.get('fName') 
        lName = request.args.get('lName')
        module._createStudent(int(studId), int(age), bytes(fName, 'utf-8'), bytes(lName, 'utf-8'))

    def getParticularStudent(self, module):
        studId = request.args.get('studId')
        return module._getParticularStudent(int(studId))

    def getStudents(self, module):
        return module._getStudents()


        