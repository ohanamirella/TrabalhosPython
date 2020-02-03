import MySQLdb
from Model.linguagem_model import LinguagemBeckModel

class LinguagemDao:

    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans', user='padawans', passwd='vm2019')
    cursor = conexao.cursor()

    def insert(self, linguagem:LinguagemBeckModel):
        inserir = f""" 
            INSERT INTO tb_linguagem (
                nome_linguagem, 
                desc_linguagem
            )
            VALUES (
                {linguagem.id_linguagem},
                '{linguagem.nome_linguagem}',
                '{linguagem.desc_linguagem}'
            )
        """
        self.cursor.execute(inserir)
        self.conexao.commit()
        id_linguagem_inserido = self.cursor.lastrowid
        return id_linguagem_inserido

    def read(self, id):
        ler = f""" 
            SELECT * FROM tb_linguagem
            WHERE id_linguagem = {id}
        """
        self.cursor.execute(ler)
        lido = self.cursor.fetchall()
        return lido

    def update(self, linguagem:LinguagemBeckModel):
        atualizar = f"""
            UPDATE tb_equipe 
            SET 
                nome_linguagem = {linguagem.nome_linguagem}
                desc_linguagem = {linguagem.desc_linguagem}
            WHERE id_linguagem = {linguagem.id_linguagem}
        """
        self.cursor.execute(atualizar)
        self.conexao.commit()

    def delete(self, id):
        deletar = f""" 
            DELETE FROM tb_linguagem
            WHERE id_linguagem = {id}
        """
        self.cursor.execute(deletar)
        self.conexao.commit()