#--- Exercicio 2 - Dicionarios
#--- Escreva um programa que leia os dados de 11 jogadores
#--- Jogador: Nome, Posicao, Numero, PernaBoa
#--- Crie um dicionario para armazenar os dados
#--- Imprima todos os jogadores e seus dados

# cerveja ['marca'] = (input('Digite a marca'))

dicionario_jogador = {}
for i in range(1,11):
    dicionario_jogador = {'Nome':'','posição':'','numero':'','pernaboa':''}
    dicionario_jogador ['nome'] = (input('Digite o nome: '))
    dicionario_jogador ['posicao'] = (input('Digite a posicao: '))
    dicionario_jogador ['numero'] = (float(input('Digite o numero: ')))
    dicionario_jogador ['pernaboa'] = (input('Digite a perna boa: '))

    print (f"Nome- {dicionario_jogador ['nome']}  Posição - {dicionario_jogador['posicao']} Número: - {dicionario_jogador['numero']} Pernaboa- {dicionario_jogador['pernaboa']}")


