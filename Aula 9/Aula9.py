# Aula 9 - 19-11-2019
#--- Crie um programa que:
#--- 1- Leia dois numeros inteiros
#--- 2- Calcule a soma entre os dois numeros atraves de um metodo
#--- 3- Calcule a subtracao entre os dois numeros atraves de um metodo
#--- 4- Calcule a multiplicacao entre os dois numeros atraves de um metodo
#--- 5- Calcule a divisao inteira entre os dois numeros atraves de um metodo
#--- 6- Calcule a divisao fracionada entre os dois numeros atraves de um metodo
#--- 7- Calcule resto da divisao entre os dois numeros atraves de um metodo
#--- 8- Calcule a raiz entre os dois numeros atraves de um metodo
#--- 9- Separa os metodos em outro arquivo 

#--- soma Tarcisio
#--- subtracao Vitor
#--- multi Nathan
#--- div int Victor
#--- div frac Pedro
#--- resto Renan
#--- raiz George

from calculo import soma, subtracao, multiplicacao, div, divF, restodiv, raiz

n1 = int(input('\n Digite um numero: '))
n2 = int(input('\n Digite outro numero: '))

print(f'\n A soma entre {n1} e {n2} é: {soma(n1,n2)}')
print(f'\n A subtração entre {n1} e {n2} é: {subtracao(n1,n2)}')
print(f'\n A multiplicaçao entre {n1} e {n2} é: {multiplicacao(n1,n2)}')
print(f'\n A divisao inteira entre {n1} e {n2} é: {div(n1,n2)}')
print(f'\n A divisão fracionária entre {n1} e {n2} é: {divF(n1,n2)}')
print(f'\n O resto da divisão entre {n1} e {n2} é: {restodiv(n1,n2)}')
print(f'\n A raiz é: {raiz(n1,n2)}')