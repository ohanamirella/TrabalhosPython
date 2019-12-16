#while bole:
#   n = n +1
bole = True
n = 0

while n >= 30:
    n = n +1
    print(f'Olá beninas{n}')
    if n == 10:
        continue
    print ('Passou!')


######################################
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

#######################################

# Criar um programa para cadastro do cliente 
# Para cadastro de clientes  deve pedir os seguintes dados:
# Codigo do cliente, CPF, Nome completo,
# data de nascimento, Estado, Cidade, cep, bairro, rua,
# número de casa, completo.

# cod_Cliente = input('Codigo de cliente: )
# cpf = input ('CPF')
#

def cadastreo_client(numero_funcao)
    dados_cliente = ['Codigo_cliente', 'CPF', 'nome_completo',
                'data_de_nascimento','estado', 'cidade'
                'cep', 'bairro','rua', 'numero_casa','complemento']
               
lista = []
dicionario = {}

numero =int(input('Digite numero '))

    for j in range(numero):
    dicionario = {}

    for i in dados_cliente:
        dicionario[i] = input(f'{i}')
    dicionario[i] = (input(f'{i}: '))
lista.append(dicionario)

print (dicionario)
print (lista)
