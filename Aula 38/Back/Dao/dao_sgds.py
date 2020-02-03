import MySQLdb
from Model.sgbds_model import SgbdsModel

class SgbdsDao:

    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans', user='padawans', passwd='vm2019')
    cursor = conexao.cursor()

    def insert(self, sgbds:SgbdsModel):
        inserir = f""" 
            INSERT INTO tb_sgbds (
                id_sgbds,
                sgbd, 
                desc_sgbd
            )
            VALUES (
                {sgbds.id_sgbds},
                '{sgbds.sgbd}',
                '{sgbds.desc_sgbd}'
            )
        """
        self.cursor.execute(inserir)
        self.conexao.commit()
        id_sgbds_inserido = self.cursor.lastrowid
        return id_sgbds_inserido

    def read(self, id):
        ler = f""" 
            SELECT * FROM tb_sgbds
            WHERE id_sgbds = {id}
        """
        self.cursor.execute(ler)
        lido = self.cursor.fetchall()
        return lido

    def update(self, sgbds:SgbdsModel):
        atualizar = f"""
            UPDATE tb_sgbds 
            SET 
                id_sgbds = {sgbds.id_sgbds}
                sgbds = '{sgbds.sgbds}'
                desc_sgbds = '{sgbds.desc_sgbds}'
            WHERE id_sgbds = {sgbds.id_sgbds}
        """
        self.cursor.execute(atualizar)
        self.conexao.commit()

    def delete(self, id):
        deletar = f""" 
            DELETE FROM tb_sgbds
            WHERE id_sgbds = {id}
        """
        self.cursor.execute(deletar)
        self.conexao.commit()