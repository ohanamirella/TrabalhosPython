import MySQLdb
from Model.sgds import sgds

class FrameworkDao:
    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans', user='padawans', passwd='ts2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM TB_SGDS AS S LEFT JOIN TB_EQUIPE AS E ON F.ID_SGDS = E.ID_EQUIPE"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM TB_SGDS AS S LEFT JOIN TB_SGDS AS E ON F.ENDERECO_ID = E.ID WHERE L.ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, sgds:Sgds:
        comando = f""" INSERT INTO TB_SGDS
        (
            ID,
            SGDS,
            DESC
        )
        VALUES
        (
            '{sgds.id}',
            '{sgds.sgbd}',
            {sgds.desc},
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, sgds:Sgds):
        comando = f""" UPDATE TB_SGDS
        SET
            ID = '{sgds.id}',
            SGDS ='{sgds.sgds}',
            DESC = {sgds.desc}
        WHERE ID = {sgds.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM TB_SGDS WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()