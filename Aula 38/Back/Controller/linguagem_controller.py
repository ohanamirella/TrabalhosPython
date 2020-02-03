from Dao.linguagem_dao import LinguagemBeckModel, LinguagemDao

class LinguagemController:
    dao = LinguagemDao()

    def read(self, id):
        tupla = self.dao.read(id)
        linguagem_model = EquipeModel(tupla[0], tupla[1], tupla[2])
        return linguagem_model

    def insert(self, linguagem_model:LinguagemBeckModel):
        insert = LinguagemDao()
        insert.insert(linguagem_model)

    def update(self, linguagem_model:LinguagemBeckModel):
        self.dao.update(framework_model)

    def delete(self, id):
        self.dao.delete(id)