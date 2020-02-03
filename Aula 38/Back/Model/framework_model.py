class FrameworkModel:

    def __init__(self, nome_framework, desc_framework):
        self.id_framework = 0
        self.nome_framework = nome_framework
        self.desc_framework = desc_framework

    def __str__(self):
        return f'{self.id_framework};{self.nome_framework};{self.desc_framework};'