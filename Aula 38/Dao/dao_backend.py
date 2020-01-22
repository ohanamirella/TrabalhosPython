#import MySQLdb
#from Model.pessoa import Pessoa

class BackendDao:
    conexao = MySQLdb.connect(host='mysql.padawan.dev', database='padawans', user='ViniMirella', passwd='ts2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM TB_EQUIPE AS P LEFT JOIN 01_MDG_ENDERECO AS E ON P.ENDERECO_ID = E.ID"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM TB_EQUIPE AS P LEFT JOIN 01_MDG_ENDERECO AS E ON P.ENDERECO_ID = E.ID WHERE P.ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, pessoa:Pessoa):
        comando = f""" INSERT INTO 01_MDG_PESSOA
        (
            NOME,
            SOBRENOME,
            IDADE,
            ENDERECO_ID
        )
        VALUES
        (
            '{pessoa.nome}',
            '{pessoa.sobrenome}',
            {pessoa.idade},
            {pessoa.endereco.id}
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, pessoa:Pessoa):
        comando = f""" UPDATE 01_MDG_PESSOA
        SET
            NOME = '{pessoa.nome}',
            SOBRENOME ='{pessoa.sobrenome}',
            IDADE = {pessoa.idade},
            ENDERECO_ID = {pessoa.endereco.id}
        WHERE ID = {pessoa.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM 01_MDG_PESSOA WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()