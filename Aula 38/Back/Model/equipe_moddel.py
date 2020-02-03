class EquipeModel:

    def __init__(self):
        self.id_equipe = 0
        self.nome_equipe = ''
        self.numero_equipe = 0
        self.descricao_equipe = ''
        self.tb_framework_id = 'NULL'
        self.tb_linguagem_id = 'NULL'
        self.tb_sgbds_id = 'NULL'
    
    def __str__(self):
        return f'{self.id_equipe};{self.nome_equipe};{self.numero_equipe};{self.descricao_equipe};{self.tb_framework_id};{self.tb_linguagem_id};{self.tb_sgbds_id};'
