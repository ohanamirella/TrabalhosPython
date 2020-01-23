import MySQLdb
from Model.linguagem import linguagem

class FrameworkDao:
    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans', user='padawans', passwd='ts2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM TB_LINGUAGEM AS L LEFT JOIN TB_EQUIPE AS E ON F.ID_LINGUAGEM = E.ID_EQUIPE"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM TB_LINGUAGEM AS L LEFT JOIN TB_LINGUAGEM AS E ON F.ENDERECO_ID = E.ID WHERE L.ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, framework:Framework):
        comando = f""" INSERT INTO TB_LINGUAGEM
        (
            ID,
            NOME,
            DESC
        )
        VALUES
        (
            '{linguagem.id}',
            '{linguagem.sgbd}',
            {linguagem.desc},
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, linguagem:Linguagem):
        comando = f""" UPDATE TB_LINGUAGEM
        SET
            ID = '{linguagem.id}',
            NOME ='{linguagem.nome}',
            IDADE = {linguagem.idade},
            DESC = {linguagem.desc}
        WHERE ID = {linguagem.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM TB_LINGUAGEM WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()