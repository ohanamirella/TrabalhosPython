#
class Backend:
    def __init__(self):
        self.id = 0
        self.nome_equipe = ''
        self.numero_equipe= ''
        self.descricao_equipe = 0
        #self.framework = ''
        #self.linguagem_id = ''
        #
    def __str__(self):
        return f'{self.id};{self.nome_equipe};{self.numero_equipe};{self.descricao_equipe};'

backend = Backend()