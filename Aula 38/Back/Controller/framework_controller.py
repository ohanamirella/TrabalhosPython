from Dao.framework_dao import FrameworkDao, FrameworkModel

class FrameworkController:
    dao = FrameworkDao()

    def read(self, id):
        tupla = self.dao.read(id)
        framework_model = EquipeModel(tupla[0], tupla[1], tupla[2])
        return framework_model

    def insert(self, framework_model:FrameworkModel):
        insert = FrameworkDao()
        insert.insert(framework_model)

    def update(self, framework_model:FrameworkModel):
        self.dao.update(framework_model)

    def delete(self, id):
        self.dao.delete(id)