class SgbdsModel:

    def __init__(self, sgbd, desc_sgbd):
        self.id_sgbds = 0
        self.sgbd = sgbd
        self.desc_sgbd = desc_sgbd

    def __str__(self):
        return f'{self.id_sgbds};{self.sgbd};{self.desc_sgbd};'