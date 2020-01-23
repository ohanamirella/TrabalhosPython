class Linguagem:
    def __init__(self):
        self.id = 0
        self.nome = ''
        self.desc = ''
      
    def __str__(self):
        return f'{self.id};{self.nome};{self.desc}'