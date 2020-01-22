from Dao.pessoa_dao import PessoaDao
from Model.pessoa import Pessoa
from Model.endereco import Endereco
from Controller.endereco_controller import EnderecoController

class PessoaController:
    dao = sqaudeDao()
    endereco_controller = EnderecoController()

    def listar_todos(self):
        lista_pessoas = []
        lista_tuplas = self.dao.listar_todos()
        for p in lista_tuplas:
            pessoa = Pessoa()
            pessoa.id =  p[0]
            pessoa.nome = p[1]
            pessoa.descricao = p[2]
            pessoa.numerodepessoas = p[3]
            pessoa.linguagembackend = Endereco()
            pessoa.frameworkfrontend = p[5]
            lista_pessoas.append(pessoa)
        return lista_pessoas

    def buscar_por_id(self, id):
        p = self.dao.buscar_por_id(id)
        pessoa = Pessoa()
        pessoa.id =  p[0]
        pessoa.nome = p[1]
        pessoa.desricao = p[2]
        pessoa.numerodepessoas = p[3]
        pessoa.linguagembackend= p[5]
        pessoa.frameworkfrontend= p[6]
        return pessoa

    def salvar(self, pessoa:Pessoa):
        pessoa.endereco.id = self.endereco_controller.salvar(pessoa.endereco)
        return self.dao.salvar(pessoa)

    def alterar(self, pessoa:Pessoa):
        self.endereco_controller.alterar(pessoa.endereco)
        self.dao.alterar(pessoa)

    def deletar(self, id):
        self.dao.deletar(id)