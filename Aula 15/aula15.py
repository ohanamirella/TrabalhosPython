# Aula 15 - 28-11-2019
# Manipulação de arquivos

def salvar(pessoa_dicionario):
    arquivo = open('aula15.txt','a')
    arquivo.write (f"{pessoa_dicionario['nome']};{pessoa_dicionario['sobrenome']};{pessoa_dicionario['idade']}\n")
    arquivo.close()

def ler():
    lista = []
    arquivo = open('aula15.txt','r')
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        pessoa = {'nome':lista_linha[0],'sobrenome':lista_linha[1],'idade':lista_linha[2]}
        print(lista_linha)
        lista.append(pessoa)
    arquivo.close()
    return lista

nome = input('Digite nome: ')
sobrenome = input('Digite o sobrnome: ')
idade = int(input('Digite idade: '))

pessoa ={'nome':nome,'sobrenome':sobrenome,'idade':idade}
salvar(pessoa)

lista = ler()
for p in lista:
    print(f"{p['nome']} - {p['sobrenome']} - {p['idade']}")


#arquivo = open('aula15.txt','r')
#for linha in arquivo:
#    print(linha)
#arquivo.close()