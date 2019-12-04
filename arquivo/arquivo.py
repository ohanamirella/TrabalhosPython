# Para abrir um arquivo para leitura

arquivo = open('cadastro.txt','r')
#conteudo = arquivo read

# lista_do_arquivo = conteudo 

for linha in arquivo:
    # print(linha)
    campos = linha.split(',')

    #print(f'{campos[1]}:{campos[3]}')
    for campo in campos:
        print(campo,)

def ler_cadastro():
    arquivo = open('18-Aula/exercicios/cadastro.txt','r')
    lista = []
    for pessoas in arquivos:
        pessoa = pessoas.strip().s´lit(';')
        dicionario = {'codigo':pessoa[0],'mome':pessoas[1]
                       'sexo':pessoas[2],'idade':pessoas[3]}
[{'codigo':'1','nome':'fernanda de almeida','sexo':'f','idade':'18'}
 {'codigo':'2','nome':'pedro almeida','sexo':'m','idade':'17'}
 {'codigo':'3','nome':'Jovana Francisca','sexo':'f','idade':'16'}
 {'codigo':'4','nome':'Mirella Ohana Bardini','sexo':'f','idade':'20'}]                       

def lista_festa(lista_de_entradas):
    for pessoa in lista_de_entradas:
        if int(pessoa['idade']) >= 18:
            lista_mulheres.append(pessoa)
        else:
            lista_homens.append(pessoa)
    salvar(lista_homens,'homens')
    salvar(lista_mulheres,'mulheres')

def salvar(lista_consulta_funcao,numero):
    arquivo = open (f'18-Aula/exercicios/{nome}.txt','a')
    for pessoa in lista:
        texto = f"{pessoa['codigo']};{pessoa['nome']};{pessoa['sexo']};{pessoa['idade']}\n"
        arquivo.write(texto)
    arquivo.close()
def consulta(lista_consulta):
    if int(lista_consulta['idade']) >= 18:
        if lista_consulta []


