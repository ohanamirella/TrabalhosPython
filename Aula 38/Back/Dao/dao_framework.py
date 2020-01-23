import MySQLdb
from Model.framework import framework

class FrameworkDao:
    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans', user='padawans', passwd='ts2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM TB_FRAMEWORK AS F LEFT JOIN TB_EQUIPE AS E ON F.ID_FRAMEWORK = E.ID_EQUIPE"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM TB_FRAMEWORK AS F LEFT JOIN TB_FRAMEWORK AS E ON F.ENDERECO_ID = E.ID WHERE F.ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, framework:Framework):
        comando = f""" INSERT INTO TB_FRAMEWORK
        (
            ID,
            NOME,
            DESC
        )
        VALUES
        (
            '{framework.id}',
            '{framework.sgbd}',
            {framework.desc},
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, framework:Framework):
        comando = f""" UPDATE TB_FRAMEWORK
        SET
            ID = '{framework.id}',
            NOME ='{framework.nome}',
            IDADE = {framework.idade},
            DESC = {framework.desc}
        WHERE ID = {framework.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM TB_FRAMEWORK WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()