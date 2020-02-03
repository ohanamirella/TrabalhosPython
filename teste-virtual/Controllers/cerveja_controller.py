from flask_restful import Resource

class CervejaController(Resource):
    def get(sell):
        return 'Acessamdo controladora pelo metodo HTTP GET'
    def post(self):
        return 'Acessando controladora pelo método HTML POST'
    def put(self):
        return 'Acessando controladora pelo método HTTP PUT'
    def delete(self):
        return 'Acessando controladora pelo método HTTP DELETE'