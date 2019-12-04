# Aula 7 - 14-11-2019
# Dicionários

#--- Criação de uma variável tipo dicionário 
dicionario = { 'Nome':'Maykon', 'Sobrenome':'Granemann' }
#--- Impressão de um dicionário completo
print(dicionario)
#--- Impressão de um dos dados do dicionário através da chave
print(dicionario['Sobrenome'])

#--- Criação de dicionário através de variávieis de tipos distintos
nome= 'Mirella'
lista_notas = [10,20,50,70]
media = sum(lista_notas)/ len(lista_notas)
situacao = 'Reprovado'
if media >=7:
    situacao = 'Aprovado'
dicionario_alunos = {'Nome':nome, 'Lista_Notas':lista_notas, 'Media': media, 'Situacao':situacao}
#--- Impressão de dados do dicionário através de suas chaves
print(f"{dicionario_alunos['Nome']} - {dicionario_alunos['Situacao']}")

#--- Criação de um dicionário com valores padrão e alteração do valor posterior a criação
dicionario_bandas = {'Nome':''}
#--- Alteração do valor através da chave
dicionario_bandas['Nome'] = 'Calipso'
print(dicionario_bandas)

#--- Criação de um dicionario e adição de uma nova chave após a criação
dicionario = { 'Nome':'Maykon', 'Sobrenome':'Granemann' }
dicionario['Sobrenome'] = 'Rauen'
#--- Adição de nova chave/valor ao dicionário existente
dicionario['CPF'] = '053.555.666-75'

#--- Criação de um dicionário com dados de uma pessoa e através do laço de repetição adicinar em lista
lista_pessoas = []
for i in range(1,11):
    dicionario_pessoa = {'Nome':'', 'Sobrenome':'', 'CPF':'', 'RG':'' }
    dicionario_pessoa['Nome'] = input('Digite o nome:' )
    dicionario_pessoa['Sobrenome'] = input('Digite o Sobrenome:' )
    dicionario_pessoa['CPF'] = input('Digite o cpf:' )
    dicionario_pessoa['RG'] = input('Digite o rg:' )
    lista_pessoas.append(dicionario_pessoa)