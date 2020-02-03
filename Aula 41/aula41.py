from flask import Flask
from flask_restful import Api
from Controller.pessoa_controller import PessoaController
app = Flask(__name__)
api = Api(app)

api.add_resource(PessoaController,'/api/pessoa')
@app.route('/')
def inicio ():
    return 'Bem vindo!'\
           '\n'\
           ':P'


app.run(debug=True, port=80)