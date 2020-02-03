Learn more or give us feedback
from flask import Flask, render_template, request, redirect
import sys
sys.path.append('C:/Users/900166/Documents/Vinicius HBSIS/Aula-Python-HBSIS/Atividade_V_M/Tarefa')
from Controller.equipe_controller import EquipeController, EquipeDao, EquipeModel
from Controller.framework_controller import FrameworkController, FrameworkDao, FrameworkModel
from Controller.linguagem_controller import LinguagemController, LinguagemBeckModel, LinguagemDao
from Controller.sgbds_controller import SgbdsController, SgbdsDao, SgbdsModel

app = Flask(__name__)
equipe_controller = EquipeController()
framework_controller = FrameworkController()
linguagem_controller = LinguagemController()
sgbds_controller = SgbdsController()

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/cadastrar')
def cadastrar():
    equipe = EquipeModel()
    equipe.linguagem = LinguagemBeckModel()
    equipe.framework = FrameworkModel()
    equipe.sgbds = SgbdsModel()

    if 'id' in request.args:
        id = request.args['id']
        equipe = equipe_controller.read(id)
    return render_template('cadastrar.html', equipe = equipe)
    

@app.route('/listar')
def listar():        
    equipe = equipe_controller.read()
    return render_template('listar.html', lista = equipe)

@app.route('/salvar')
def salvar():
    equipe = EquipeModel()
    # equipe.id_equipe = request.args['id_equipe']
    equipe.nome_equipe = request.args['nome_equipe']
    equipe.numero_equipe = request.args['numero_equipe']
    equipe.descricao_equipe = request.args['descricao_equipe']

    linguagem = LinguagemBeckModel()
    # linguagem.id_linguagem = request.args['id_linguagem']
    linguagem.nome_linguagem = request.args['nome_linguagem']
    linguagem.desc_linguagem = request.args['desc_linguagem']

    sgbds = SgbdsModel()
    # sgbds.id_sgbds = request.args['id_sgbds']
    sgbds.sgbd = request.args['sgbd']
    sgbds.desc_sgbd = request.args['desc_sgbd']

    framework = FrameworkModel()
    # framework.id_framework = request.args['id_framework']
    framework.nome_framework = request.args['nome_framework']
    framework.desc_framework = request.args['desc_framework']

    equipe.linguagem = linguagem
    equipe.sgbds = sgbds
    equipe.framework = framework

    if equipe.id_equipe == 0:
        equipe_controller.update(equipe)
    else:
        equipe_controller.update(equipe)
    return redirect('/listar')

@app.route('/excluir')
def excluir():
    id_equipe = int(request.args['id_equipe'])
    id_linguagem = request.args['id_linguagem']
    id_framework = request.args['id_framework']
    id_sgbds = request.args['id_sgbds']
    equipe_controller.delete(id)

    if id_equipe != 'None':
        equipe_controller.delete(id_equipe)
    return redirect('/listar')

    if id_framework != 'None':
        framework_controller.delete(id_framework)
    return redirect('/listar')

    if id_linguagem != 'None':
        linguagem_controller.delete(id_linguagem)
    return redirect('/listar')

    if id_sgbds != 'None':
        sgbds_controller.delete(id_sgbds)
    return redirect('/listar')

app.run(debug=True)