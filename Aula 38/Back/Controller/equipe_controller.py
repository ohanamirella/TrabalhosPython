from Dao.equipe_dao import EquipeDao, EquipeModel
from Controller.framework_controller import FrameworkController
from Controller.linguagem_controller import LinguagemController
from Controller.sgbds_controller import SgbdsController

class EquipeController:
    dao = EquipeDao()
    framework_controller = FrameworkController()
    linguagem_controller = LinguagemController()
    sgbds_controller = SgbdsController()

    def read(self, id):
        tupla = self.dao.read(id)
        equipe_model = EquipeModel(tupla[0], tupla[1], tupla[2], tupla[3])
        equipe_model.tb_framework_id = tupla[4]
        equipe_model.tb_linguagem_id = tupla[5]
        equipe_model.tb_sgbds_id = tupla[6]
        return equipe_model


    def insert(self, equipe_model:EquipeModel):
        insert = EquipeDao()
        insert.insert(equipe_model)

    def update(self, equipe_model:EquipeModel):
        self.dao.update(equipe_model)

    def delete(self, id):
        self.dao.delete(id)