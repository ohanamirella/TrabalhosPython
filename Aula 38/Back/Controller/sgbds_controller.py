from Dao.pessoa_dao import PessoaDao
from Model.pessoa import Pessoa
from Model.endereco import Endereco
from Controller.endereco_controller import EnderecoController

class PessoaController:
    dao = PessoaDao()
    endereco_controller = EnderecoController()

    def listar_todos(self):
        lista_pessoas = []
        lista_tuplas = self.dao.listar_todos()
        for p in lista_tuplas:
            pessoa = Pessoa()
            pessoa.id =  p[0]
            pessoa.nome = p[1]
            pessoa.sobrenome = p[2]
            pessoa.idade = p[3]
            pessoa.endereco = Endereco()
            pessoa.endereco.id = p[5]
            pessoa.endereco.logradouro = p[6]
            pessoa.endereco.numero = p[7]
            pessoa.endereco.complemento = p[8]
            pessoa.endereco.bairro = p[9]
            pessoa.endereco.cidade = p[10]
            pessoa.endereco.cep = p[11]
            lista_pessoas.append(pessoa)
        return lista_pessoas

    def buscar_por_id(self, id):
        p = self.dao.buscar_por_id(id)
        pessoa = Pessoa()
        pessoa.id =  p[0]
        pessoa.nome = p[1]
        pessoa.sobrenome = p[2]
        pessoa.idade = p[3]
        pessoa.endereco.id = p[5]
        pessoa.endereco.logradouro = p[6]
        pessoa.endereco.numero = p[7]
        pessoa.endereco.complemento = p[8]
        pessoa.endereco.bairro = p[9]
        pessoa.endereco.cidade = p[10]
        pessoa.endereco.cep = p[11]
        return pessoa

    def salvar(self, pessoa:Pessoa):
        pessoa.endereco.id = self.endereco_controller.salvar(pessoa.endereco)
        return self.dao.salvar(pessoa)

    def alterar(self, pessoa:Pessoa):
        self.endereco_controller.alterar(pessoa.endereco)
        self.dao.alterar(pessoa)

    def deletar(self, id):
        self.dao.deletar(id)