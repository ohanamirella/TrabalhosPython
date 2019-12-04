print("*"*50)
print('FESTIVAL DE CERVEJA EM INTURORÓ')
print("*"*50)

menu = ('1-Cadastro de cliente\n2-Ver cliente cadastrados\n3-Cadastro de produtos\n4-Ver produtos cadastrados\n5-Vendas\n6-Relatório de vendas\n6-Sair\n\n\nDigite a opção desejada:')

opcao = input(menu)
while True:
    opcao = input(menu)
    if opcao == '1':
        print('Cadastro de Cliente')
    elif opcao == '2':
        print('Ver cliente cadastrados')
    elif opcao == '3':
        print('Cadastro de produtos')
    elif opcao == '4':
        print('Ver produtos cadastrados')
    elif opcao == '5':
        print('Vendas')
    elif opcao == '6':
        print('Relatório de vendas')
    elif opcao == '7' :
        print('SAIR')
        break
    else: 
        print('Valor invalido')
