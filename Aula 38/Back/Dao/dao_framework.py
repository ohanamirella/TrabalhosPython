import MySQLdb
from Model.framework_model import FrameworkModel

class FrameworkDao:
    
    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans', user='padawans', passwd='vm2019')
    cursor = conexao.cursor()

    def insert(self, framework_model:FrameworkModel):
        inserir = f""" 
            INSERT INTO tb_framework (
                nome_framework,
                desc_framework
            )
            VALUES (
                '{framework_model.nome_framework}',
                '{framework_model.desc_framework}',
            )
        """
        self.cursor.execute(inserir)
        self.conexao.commit()
        id_frame_inserido = self.cursor.lastrowid
        return id_frame_inserido

    def read(self, id):
        ler = f""" 
            SELECT * FROM tb_framework
            WHERE id_framework = {id}
        """
        self.cursor.execute(ler)
        lido = self.cursor.fetchone()
        return lido

    def update(self, framework_model:FrameworkModel):
        atualizar = f"""
            UPDATE tb_framework 
            SET 
                nome_framework = {framework_model.nome_framework}, 
                desc_framework = {framework_model.desc_framework},
            WHERE id_framework = {framework_model.id_framework}
        """
        self.cursor.execute(atualizar)
        self.conexao.commit()

    def delete(self, id):
        deletar = f""" 
            DELETE FROM tb_framework
            WHERE id_framework = {id}
        """
        self.cursor.execute(deletar)
        self.conexao.commit()