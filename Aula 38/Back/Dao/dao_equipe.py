import MySQLdb
from Model.equipe_model import EquipeModel

class EquipeDao:
    
    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans', user='padawans', passwd='vm2019')
    cursor = conexao.cursor()

    def insert(self, equipe_model:EquipeModel):
        inserir = f""" 
            INSERT INTO tb_equipe (
                nome_equipe, 
                numero_equipe,
                descricao_equipe,
                tb_framework_id,
                tb_linguagem_id,
                tb_sgbds_id
            )
            VALUES (
                {equipe_model.id_equipe},
                '{equipe_model.nome_equipe}',
                {equipe_model.numero_equipe},
                '{equipe_model.descricao_equipe}',
                {equipe_model.tb_framework_id},
                {equipe_model.tb_linguagem_id},
                {equipe_model.tb_sgbds_id}
            )
        """
        self.cursor.execute(inserir)
        self.conexao.commit()
        id_equipe_inserido = self.cursor.lastrowid
        return id_equipe_inserido

    def read(self, id):
        ler = f""" 
            SELECT * FROM tb_equipe
            left JOIN tb_framework
            ON id_framework = tb_framework_id
            left JOIN tb_linguagem 
            ON id_linguagem = tb_linguagem_id
            left JOIN tb_sgbds
            ON id_sgbds = tb_sgbds_id
            WHERE id_equipe = {id}
        """
        self.cursor.execute(ler)
        lido = self.cursor.fetchone()
        return lido

    def update(self, equipe:EquipeModel):
        atualizar = f"""
            UPDATE tb_equipe 
            SET 
                id_equipe = {equipe.id_equipe},
                nome_equipe = {equipe.nome_equipe}, 
                numero_equipe = {equipe.numero_equipe},
                descricao_equipe = {equipe.descricao_equipe},
                tb_framework_id = {equipe.tb_framework_id},
                tb_linguagem_id = {equipe.tb_linguagem_id},
                tb_sgbds_id = {equipe.tb_sgbds_id},
            WHERE id_equipe = {equipe.id_equipe}
        """
        self.cursor.execute(atualizar)
        self.conexao.commit()

    def delete(self, id):
        deletar = f""" 
            DELETE FROM tb_equipe
            WHERE id_equipe = {id}
        """
        self.cursor.execute(deletar)
        self.conexao.commit()