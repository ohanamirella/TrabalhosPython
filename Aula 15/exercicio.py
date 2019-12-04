# Aula 15 - 27-11-2019
# Dicionários 
# Aula 15 - 28-11-2019
# Manipulação de arquivos

def salvar_cerveja(cerveja_dicionario):
    arquivo = open('exaula15.txt','a')
    arquivo.write(f"{pessoa_dicionario['nome']};{pessoa_dicionario['marca']};{pessoa_dicionario['teor']};{pessoa_dicionario['tipo']}\n")
    arquivo.close()

def ler():
    lista = []
    arquivo = open('exaula15.txt','r')
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
       cerveja = {'nome':lista_linha[0], 'marca':lista_linha[1], 'teor':lista_linha[2], 'tipo':lista_linha[3]}
        lista.append(pessoa)
    arquivo.close()
    return lista

nome  = input('Digite o nome da cerveja : ')
marca = input('Digite a marca da cerveja : ')
teor = int(input('Digite o teor : '))
tipo = input('Digite o tipo da cerveja : ')

cerveja = {'nome':nome, 'marca':marca, 'teor':teor, 'tipo':tipo}


for p in ler():
    print(f"{p['nome']} - {p['marca']} - {p['teor']} - {p['tipo']}")