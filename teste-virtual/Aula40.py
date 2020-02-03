from flask import Flask
from flask_restfull import Api
from Controllers.cerveja_controller import CervejaController
#GET
#POST
#PUT
#DELETE


app = Flask(__name__)
api = Api(app)

api.add_resource(CevejaContoller,'/api/cerveja')
@app.route('/')
def inicio ():
    return 'Bem vindo API'

app.run(debug=True, port=80)