from Model.endereco import Endereco
class Pessoa:
    def __init__(self):
        self.id = 0
        self.nome = ''
        self.descricao= ''
        self.numerodepessoas = 0
        self.linguagembackend= ''
        self.ende = Endereco()

    def __str__(self):
        return f'{self.id};{self.nome};{self.sobrenome};{self.idade};{self.endereco}'

pessoa = Pessoa()