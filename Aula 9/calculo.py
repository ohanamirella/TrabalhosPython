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

def soma (n1, n2):
    total = n1 + n2
    return total

def subtracao (n1,n2):
    subtracao = n1 - n2
    return subtracao

def multiplicacao (n1,n2):
    multiplicacao = n1 * n2
    return multiplicacao

def div(n1,n2):
    div = n1 // n2
    return div

def divF(n1, n2):
    divF = n1 / n2
    return divF

def restodiv(n1, n2):
    restodiv = n1 % n2
    return restodiv

def raiz (n1,n2):  # n1 = radicando n2= indice da raiz 
    raiz = n1 ** (1/n2)
    return raiz