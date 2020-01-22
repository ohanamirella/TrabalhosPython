# pip3 install flask_mysqldb
# referencia ao Mysql

import MySQLdb


#listar todas as pessoas 
def listar_todos(c):
    c.execute('SELECT * FROM 01_MDG_PESSOA')
    pessoas = c.fetchall()
    for p  in  pessoas:
        print(p)

#buscar uma pessoa pelo ID
def buscar_por_id(c, id):
    c.execute(f'SELECT * FROM 01_MDG_PESSOA WHERE ID = {id}')
    pessoa = c.fetchone()
    print(pessoa)

#buscar pessoas por sobrenome
def buscar_por_sobrenome(c, sobrenome):
    c.execute(f"SELECT * FROM 01_MDG_PESSOA WHERE SOBRENOME like '{sobrenome}%' ")
    for p  in  c.fetchall():
        print(p)

#salvar pessoa
def salvar(cn, cr, nome, sobrenome, idade, endereco_id='NULL'):
    cr.execute(f"INSERT INTO 01_MDG_PESSOA (NOME, SOBRENOME, IDADE, ENDERECO_ID )VALUES('{nome}', '{sobrenome}',{idade},{endereco_id})")
    cn.commit()

#alterar pessoa
def alterar(cn, cr, id, nome, sobrenome, idade, endereco_id='NULL'):
    try:
        cr.execute(f"UPDATE 01_MDG_PESSOA SET NOME='{nome}', SOBRENOME='{sobrenome}', IDADE={idade}, ENDERECO_ID={endereco_id} WHERE ID={id} ")
        cn.commit()
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        if(e.args[0]==1452):
            print(f"Erro de Foreign Key jovem, id errado")

#deletar pessoa por ID
def deletar(cn, cr, id):
    cr.execute(f'DELETE FROM 01_MDG_PESSOA WHERE ID={id}')
    cn.commit()

conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019' )
cursor = conexao.cursor()

# listar_todos(cursor)
# buscar_por_id(cursor, 3)
# buscar_por_sobrenome(cursor,'Gru')
# salvar(conexao, cursor, 'Voltolini', 'KingOfFlask', 16,5)
alterar(conexao, cursor, 8, 'Gugu Voltolini', 'KingOfBasquete', 17, 6)
# deletar(conexao, cursor, 7)