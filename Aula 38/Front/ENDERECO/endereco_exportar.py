def exportar_txt(lista_enderecos):
    #----- Cria um arquivo e atribui a uma variável 'arquivo'
    with open('/Users/900163/Desktop/PythonHBSIS/Hard/ENDERECO/endereco_01/enderecoX.txt','a') as arquivo:
        #---- Percorre a lista de dicionário e salva no arquivo em formato pré-definido
        for i in lista_enderecos:
            arquivo.write(f"{i['Id']};{i['Rua']};{i['Numero']};{i['Complemento']};{i['Bairro']};{i['Cidade']}\n")