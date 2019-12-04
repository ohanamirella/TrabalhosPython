#--- Aula 2 18-11-2019
#--- Python e aplicação console - Função 

print('''Este final de semana fiquei em casa
não fui a praia e esqueci de fazer os exercíos
 deixado pelo professor na ultima aula''')

nome_completo = '\tMirella' ' ' 'Bardini\n' 

print(nome_completo)

#print((nome_completo).count('a'))
#print((nome_completo).lower())
#print((nome_completo).upper())
#print((nome_completo).split(' '))
#print((nome_completo)stript().split('i'))
#print((nome_completo).strip() )
#print((nome_completo).strip() )
#print((nome_completo).capitalize() )

pessoa = ["","Carinhoso" "Atencioso" "Querido"]

print(pessoa)
print(('nem').join(pessoa))
frase = 'Teti torrado'

print ('a'.join(frase))

print(pessoa[1:])
print(pessoa[1:3])
print(pessoa[:2]
print(frase[:5])
print(frase[5:10])
print(frase[:4])
print((pessoa.count("Carinhoso".strip().capitalize())))
########################################################################
#Aula 8 - 18-11-2019
#WEB

from flask import Flask

app = Flask(__name__)
@app.route ('/')
def inicio():
    return 'Bem vindos ao mundo real'

app.run ()
#######################################################
# Aula 8 -19-11-2019
# Tuplas

numeros = [1,4,6]
usuario = {'nome': 'user', 'passwd':123456}
pessoa = ('mirella','bardini', 0 45.5, numeros )

#print (nome)
#print (usuario)
#print (pessoa)
########################################################

