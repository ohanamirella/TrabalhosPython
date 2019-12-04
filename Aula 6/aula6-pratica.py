#Estrutura de decisão


idade = 17.5
# If sompes, validação de apenas uma condição
if (idade < 18):
        print('Dimenor')
elif (idade == 18) :
#--- if com else,
#--- Caso a condição valida pelo If não seja verdadeira,
#--- O Else é executado
   print ('Silascou')
else: 
    print('Silascou mais ainda')

#--- If comElif e else
#--- Caso a condição validada no is seja falsa
#--- É validado a condição do Elif
#--- Else é executado
# --- if COM VARIAVEL BOOLEANA
# --- Em caso de variavel booleana, não é necessário a validacao 
ativo = True

if ativo:
    print('Logar')
else:
    print ('Não pode')
###############################################################
# Aula 4_2 13-11-2019
#Booleanas

# idade = 18

# if idade == 18:
# validador = False
# Validador = True

idade = 18
validador = (idade == 18)
print (validador)

if validador: 
    print ('Maior')

idade = 18
validador - (idade ! 18)
print (validador)
 validador = (idade < 18 )
 print (validador)
 validador = (idade > 18 )
 print (validador)
 validador = (idade >= 18)
 print (validador)
  validador = (idade <= 18)
 print (validador)

 validador = not True
 validador = not False

 validador = (sorteado == 'M')
##############################################
numero1 = int(input(Digite o primeiro número))
numero2= int(input(Digite o segundo numero))

resultado =  numero1 + numero2 :
print(resultado)
resultado = numero2 - numero1 :
print(resultado)
resultado = numero1 * numero2 :
print(resultado)

resultado = numero2 / numero1 :
print(resultado)

if numero1 < numero2 :
    print('Segundo é maior do que o primeiro.')
if numero1 > numero2:
    print('Primeiro é maior do que segundo.')
if numero1 == numero2 :
    print('São iguais. ')
###########################################################
nota1(int(input('Digite a primeira nota: '))
nota2(int(input('Digite a segundo nota: '))
nota3(int(input('Digite a tereiro nota: '))
nota4(int(input('Digite a quarta nota: '))
#################################################
# Aula 6 - 13-11-2019
# Listas

#---- Inicialização de uma variável do tipo lista vazia
lista1 = []
#---- Inicialização de uma variável lista, com elementos
lista2 = ["Marcela", 'Nicole', '*Matheus']
#---- Lista de inteiros
lista3 = [1,2,3,5]
#---- lista de tipos diferentes
lista4 = [1, "Maykon", 12.5]

#---- Impressao das listas criadas
print(lista1)
print(lista2)
print(lista3)
print(lista4)

#---- Adicionando elementos em uma lista ja criada
lista1.append(lista2)
lista1.append(lista3)

#---- Impressao das listas modificadas
print(lista1)
print(lista2)
print(lista3)

#---- Criacao de lista com dados vindos da função Input
lista_perguntas = [input('Digite seu artista favorito'), input('Digite seu guitarrista favorito')] 
print(lista_perguntas)

#---- Recuperando um dado de uma posição específica da lista
posicao = int(input('Digite a posicao: '))
print( lista2[posicao-1] )
#######################################################
# Aula 6 - 13-11-2019
# Listas

#---- Inicialização de uma variável do tipo lista vazia
lista1 = []
#---- Inicialização de uma variável lista, com elementos
lista2 = ["Marcela", 'Nicole', '*Matheus']
#---- Lista de inteiros
lista3 = [1,2,3,5]
#---- lista de tipos diferentes
lista4 = [1, "Maykon", 12.5]

#---- Impressao das listas criadas
print(lista1)
print(lista2)
print(lista3)
print(lista4)

#---- Adicionando elementos em uma lista ja criada
lista1.append(lista2)
lista1.append(lista3)

#---- Impressao das listas modificadas
print(lista1)
print(lista2)
print(lista3)

#---- Criacao de lista com dados vindos da função Input
lista_perguntas = [input('Digite seu artista favorito'), input('Digite seu guitarrista favorito')] 
print(lista_perguntas)

#---- Recuperando um dado de uma posição específica da lista
posicao = int(input('Digite a posicao: '))
print( lista2[posicao-1] )
#################################################

lista_alnos = []
lista_notas = []
n1 = 0 
n2 = 1
n3 = 2
n4 = 3
 
for i in range (0,2):
    lista_alnos.append (input(f'Digite o nome do aluno {i+1} :'))
    for n in range (0,4):
        lista_notas.append (float(input(f'Digite a nota {n+1} :')))

for aluno in lista_alnos:
    media = (lista_notas[n1]+ lista_notas[n2] + lista_notas[n3] + lista_notas[n4])/4
        
    if media >=7:
        resultado = 'Aprovado'
    else :
        resultado = 'Reprovado'
    n1 += 4
    n2 += 4
    n3 += 4
    n4 += 4

print(f'Resultado: {resultado}'
#########################################################
#--- Execício 1 - listas
#--- Escreva programa que leia as notas (4) de 10 alunos
#--- Armazene os nomes em uma lista
#--- Imprima: 
#           1- O nome dos alunos
#           2- Média do aluno
#           3- Resultado (Aprovado >= 7.0)

nome = (input('Digite o nome do aluno(a) 1: '))

# lista = ['Mirella','Marcela', 'Thalyta','Nicole', 'Talissa', 'Matheus', 'Ricardo', 'André', 'Lucas', 'Felipe']
# for i in range(0,1):
#     print(lista[i])
# if Lista = ['Mirella','Marcela', 'Thalyta','Nicole', 'Talissa', 'Matheus', 'Ricardo', 'André', 'Lucas', 'Felipe']


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segundo nota: '))
nota3 = float(input('Digite a tereira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
print (f'{media}')

if media >= 7:
    print('Aluno aprovado')
else :
    print('Aluno reprovado')

print (f'Aluno(a): {nome},\n Média Final: {media}')

nome = (input('Digite o nome do aluno(a): '))

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segundo nota: '))
nota3 = float(input('Digite a tereira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
print (f'{media}')

if media >= 7:
    print('Aluno aprovado')
else :
    print('Aluno reprovado')

nome = (input('Digite o nome do aluno(a): '))

lista = ['Mirella','Marcela', 'Thalyta','Nicole', 'Talissa', 'Matheus', 'Ricardo', 'André', 'Lucas', 'Felipe']
for i in range(0,1):
    print(lista[i])
# if Lista = ['Mirella','Marcela', 'Thalyta','Nicole', 'Talissa', 'Matheus', 'Ricardo', 'André', 'Lucas', 'Felipe']


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segundo nota: '))
nota3 = float(input('Digite a tereira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
print (f'{media}')

if media >= 7:
    print('Aluno aprovado')
else :
    print('Aluno reprovado')

nome = (input('Digite o nome do aluno(a): '))

lista = ['Mirella','Marcela', 'Thalyta','Nicole', 'Talissa', 'Matheus', 'Ricardo', 'André', 'Lucas', 'Felipe']
for i in range(0,1):
    print(lista[i])
# if Lista = ['Mirella','Marcela', 'Thalyta','Nicole', 'Talissa', 'Matheus', 'Ricardo', 'André', 'Lucas', 'Felipe']


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segundo nota: '))
nota3 = float(input('Digite a tereira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
print (f'{media}')

if media >= 7:
    print('Aluno aprovado')
else :
    print('Aluno reprovado')

nome = (input('Digite o nome do aluno 5: '))

lista = ['Mirella','Marcela', 'Thalyta','Nicole', 'Talissa', 'Matheus', 'Ricardo', 'André', 'Lucas', 'Felipe']
for i in range(0,1):
    print(lista[i])
# if Lista = ['Mirella','Marcela', 'Thalyta','Nicole', 'Talissa', 'Matheus', 'Ricardo', 'André', 'Lucas', 'Felipe']


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segundo nota: '))
nota3 = float(input('Digite a tereira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
print (f'{media}')

if media >= 7:
    print('Aluno aprovado')
else :
    print('Aluno reprovado')

nome = (input('Digite o nome do aluno 6: '))

lista = ['Mirella','Marcela', 'Thalyta','Nicole', 'Talissa', 'Matheus', 'Ricardo', 'André', 'Lucas', 'Felipe']
for i in range(0,1):
    print(lista[i])
# if Lista = ['Mirella','Marcela', 'Thalyta','Nicole', 'Talissa', 'Matheus', 'Ricardo', 'André', 'Lucas', 'Felipe']


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segundo nota: '))
nota3 = float(input('Digite a tereira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
print (f'{media}')

if media >= 7:
    print('Aluno aprovado')
else :
    print('Aluno reprovado')

nome = (input('Digite o nome do aluno 7: '))

lista = ['Mirella','Marcela', 'Thalyta','Nicole', 'Talissa', 'Matheus', 'Ricardo', 'André', 'Lucas', 'Felipe']
for i in range(0,1):
    print(lista[i])
# if Lista = ['Mirella','Marcela', 'Thalyta','Nicole', 'Talissa', 'Matheus', 'Ricardo', 'André', 'Lucas', 'Felipe']


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segundo nota: '))
nota3 = float(input('Digite a tereira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
print (f'{media}')

if media >= 7:
    print('Aluno aprovado')
else :
    print('Aluno reprovado')

nome = (input('Digite o nome do aluno 8: '))

lista = ['Mirella','Marcela', 'Thalyta','Nicole', 'Talissa', 'Matheus', 'Ricardo', 'André', 'Lucas', 'Felipe']
for i in range(0,1):
    print(lista[i])
# if Lista = ['Mirella','Marcela', 'Thalyta','Nicole', 'Talissa', 'Matheus', 'Ricardo', 'André', 'Lucas', 'Felipe']


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segundo nota: '))
nota3 = float(input('Digite a tereira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
print (f'{media}')

if media >= 7:
    print('Aluno aprovado')
else :
    print('Aluno reprovado')

nome = (input('Digite o nome do aluno 9: '))

lista = ['Mirella','Marcela', 'Thalyta','Nicole', 'Talissa', 'Matheus', 'Ricardo', 'André', 'Lucas', 'Felipe']
for i in range(0,1):
    print(lista[i])
# if Lista = ['Mirella','Marcela', 'Thalyta','Nicole', 'Talissa', 'Matheus', 'Ricardo', 'André', 'Lucas', 'Felipe']


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segundo nota: '))
nota3 = float(input('Digite a tereira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
print (f'{media}')

if media >= 7:
    print('Aluno aprovado')
else :
    print('Aluno reprovado')

nome = (input('Digite o nome do aluno 10: '))

lista = ['Mirella','Marcela', 'Thalyta','Nicole', 'Talissa', 'Matheus', 'Ricardo', 'André', 'Lucas', 'Felipe']
for i in range(0,1):
    print(lista[i])
# if Lista = ['Mirella','Marcela', 'Thalyta','Nicole', 'Talissa', 'Matheus', 'Ricardo', 'André', 'Lucas', 'Felipe']


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segundo nota: '))
nota3 = float(input('Digite a tereira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
print (f'{media}')

if media >= 7:
    print('Aluno aprovado')
else :
    print('Aluno reprovado')
########################################
#--- Execício 1 - listas
#--- Escreva programa que leia as notas (4) de 10 alunos
#--- Armazene os nomes em uma lista
#--- Imprima: 
#           1- O nome dos alunos
#           2- Média do aluno
#           3- Resultado (Aprovado >= 7.0)
###############################################################
lista1 = []
lista2 = ['Marcela','Nicole','*Matheus',10]
lista3 = [0,1,2,3,4,5,6,7,8,9]

print (lista1)
print (lista2)
print (lista3)

lista1.append(lista2)
lista1.append(lista3)

lista_perguntas = (input('Digite seu artista favorito'), input('Digite seu guitarrista favorito'))
print (lista_perguntas)
posição = int(input ('Digite a posicao:'))
print (lista2 [posicao - 1])

#inicialização de uma variável lista
[]
#inicialização de uma variável lista, com elementos
lsta1 = ['Marcela', 'Nicole', '*Matheus']

#impressao das listas criadas
print (lista1)
print (lista2)
print (lista3)
print (lista3)

# ---- Imressao das listas modificadas
print (lista1)
print (lista2)
print (lista3)
print ('='*100)
#############################################################







