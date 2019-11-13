nome = (input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))

if idade >= 18 :
    print('Pode adquirir Bebidas Alcoolicas')
else :
    print('Não pode adquirir Bebidas Alcoolicas')

print('Digite o cadatro do produto')
produto = (input('Digite o nome do produto'))


categoria = (input("Digite a categoria do produto:\nAlcoolico\nNão alcoolico\n"))

print ('Produto cadastrado:',produto,'-', categoria)

if idade < 18 and categoria == 'alcoolico':
    print('Escolha outro produto')
