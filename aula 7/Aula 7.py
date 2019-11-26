# Aula 7 - 14-11-2019
# Dicionarios

lista = []
dicionario = {'nome':'mirella','sobrenome':'Bardini'}

print(dicionario)
print(dicionario['Sobrenome'])

nome = 'Mirella'
lista_notas = [10,20,50,70]
media = sum (lista_notas)/ len(lista_notas)
situacao = 'Reprvado'
if media >=7:
    situacao = 'Aprovado'
dicionario_alunos = {'Nome':nome, 'Lista_notas' :lista_notas, 'Media' :media, 'Situacao':siuacao}

print(f"{dicionario_alunos['Nome']} - {dicionario_alunos['Situacao']}")