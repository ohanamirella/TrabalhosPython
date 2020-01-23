#
class Backend:
    def __init__(self):
        self.id = 0
        self.nome = ''
        self.desc= ''
        #self.framework = ''
        #self.linguagem_id = ''
        #
    def __str__(self):
        return f'{self.id};{self.nome};{self.desc}'

backend = Backend()