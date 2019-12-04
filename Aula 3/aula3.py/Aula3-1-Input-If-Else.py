#--- Aula 3  07-11-2019
#--- Input e Estruturas de decisão

#--- Uso da função Input para a leitura de dados do tipo string
nome = input('Digite seu nome:')
sobrenome = input('Digite seu sobrenome:')
idade = int(input('Digite sua idade:'))

#--- Impressão de dados lidos pela função input
print(f'Nome:{nome} Sobrenome:{sobrenome} Idade: {idade}')

#--- Estrutura de decisão usando IF e ELSE
#--- Caso a idade seja menor que 18 o codigo abaixo do IF é executado
if idade < 18:
    print('Não pode usar mercado Tech, para o que presta')
#--- Caso a idade seja maior ou igual a 18 o codigo abaixo do else é executado
else:
    print('Pode usar mercado Tech e chapar o coco')