class LinguagemBeckModel:

    def __init__(self, nome_linguagem, desc_linguagem):
        self.id_linguagem = 0
        self.nome_linguagem = nome_linguagem
        self.desc_linguagem = desc_linguagem

    def __str__(self):
        return f'{self.id_linguagem};{self.nome_linguagem};{self.desc_linguagem};'