# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# 1 - Crie um arquivo que leia 2 números inteiros e imprima a soma, 
# multiplicação, divisão e subtração com uma f-string.

# 2 - Crie um while que pergunte se deseja continuar. Se digitar 's' o
# programa 

controle = 'n'
while conltrole != 's':
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))

    print(f'A soma de {num1} e {num2} é: {num1 + num1}')
    print(f'A divião de {num1} e  {num2} {num1 / num2}')
    print(f'A divião de {num1} e  {num2} {num1 * num2}')
    print(f'A divião de {num1} e  {num2} {num1 - num2}')

    controle = input("Digite 's' para sair...")


def inteiro(inteiro):
    arquivo = open('exaula21.txt','a')
    arquivo.write(f"Digite o primeiro numero: \n")
    arquivo.close()
