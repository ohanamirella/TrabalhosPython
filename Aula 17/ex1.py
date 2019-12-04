#Faça um menu interativo que tenha; Cadastro da banda, cadastro do album, cadastro da musica, sair
#O menu deve ser execuado até que se escolha a opção sair
#Cada opçaõ deve ser mostrada
#quando selecionado a opção sair,

lista_banda = []
lista_album = []
lista_musica = []

print('¨'*100)
print('MÚSICAS')
print('¨'*100)
menu('1-Cadastro de banda\n2-Cadastro de album\n3-Cadastr de musica\n4-sair')
opcao = input (menu)
while True: 
    opcao = input(menu)
    if opcao == '1':
        lista_banda.append(input('Digite o nome da banda:'))
    elif opcao == '2':
        lista_album.append(input('Digite o nome do album'))
    elif opcao == '3':
        lista_musica.append(input('Digite o nome da música'))

print(f'{lista_musica},{lista_album},{lista_musica}')