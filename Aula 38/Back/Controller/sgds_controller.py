from Dao.sgbds_dao import SgbdsDao, SgbdsModel

class SgbdsController:
    dao = SgbdsDao()

    def read(self, id):
        tupla = self.dao.read(id)
        sgbds_model = EquipeModel(tupla[0], tupla[1], tupla[2])
        return sgbds_model

    def insert(self, sgbds_model:SgbdsModel):
        insert = SgbdsDao()
        insert.insert(sgbds_model)

    def update(self, sgbds_model:SgbdsModel):
        self.dao.update(sgbds_model)

    def delete(self, id):
        self.dao.delete(id)