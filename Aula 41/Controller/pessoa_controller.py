from flask_restful import Resource

class PessoaController(Resource):
    def get(sell):
        return 'Acessamdo HTTP GET'
    def post(self):
        return 'Acessando HTML POST'
    def put(self):
        return 'Acessando HTTP PUT'
    def delete(self):
        return 'AcessandoHTTP DELETE'