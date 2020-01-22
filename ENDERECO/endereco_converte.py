def converter_tabela_dicionario(lista_tuplas):
    #cria uma lista para armazenar os dicionarios
    lista_endereco = []
    for p in lista_tuplas:
        #----- Criação do dicionario que representa uma pessoa
        dicionario_endereco = {'Id': 0, 'Rua' : '', 'Numero': '', 'Complemento' : '', 'Bairro': '', 'Cidade':''}
        #--- pega cada posição da tupla e atribui a uma chave do dicionário
        dicionario_endereco['Id'] = p[0]
        dicionario_endereco['Rua'] = p[1]
        dicionario_endereco['Numero'] = p[2]
        dicionario_endereco['Complemento'] = p[3]
        dicionario_endereco['Bairro'] = p[4]
        dicionario_endereco['Cidade'] = p[5]
        lista_endereco.append(dicionario_endereco)
    return lista_endereco