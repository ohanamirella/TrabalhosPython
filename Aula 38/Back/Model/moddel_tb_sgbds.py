class Backend:
    def __init__(self):
        self.id = 0
        self.sgbd = ''
        self.desc = 0
        
    def __str__(self):
        return f'{self.id};{self.sgbd};{self.desc}'

backend = Backend()