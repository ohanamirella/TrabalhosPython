# Aula 9 - 19-11-2019
#--- Crie um programa que:
#--- 1- Leia dois números inteiros
#--- 2- Calcule a soma entre os dois numeros atraves de um metodo 
#--- 3- Calcule a subtração entre os dois numeros atraves de um metodo 
#--- 4- Calcule a multiplicação entre os dois numeros atraves de um metodo
#--- 5- Calcule a divisao fracionada entre os dois numeros atraves do metodo
#--- 6- Calcule a divisao dracionada entre os dois numeros atraves de um metodo
#--- 7- Calcule resto da divisao entre os dois numeros atraves de um metodo
#--- 8- Calcule a raiz entre os dois numeros atraves de um metodo
#--- separa os metodos um do  outro


n1 = print (int(input('Digite o primeiro número inteiro :')))
n2 = print (int(input('Digite o segundo número inteiro :')))

def ():
    if(n1 + n2):
   #############################################
# Aula 9 - 19-11-2019
#--- Web2

from calculo_imposto import

def calculo_inss():
    if(salario > 0 and salario <= 1751.81):
        inss = salario * 0.08
    elif (salario > 1751.81 and salario <= 2919.72):
        inss = salario * 0.09
    elif (salario > 2919.72 and salario <= 5839.45):
        inss = salario *0.11
    else:
        inss = 642.3395

def calculo_irrf():


nome_completo = input('Digite seu nome completo:')
cpf = input('Diqite seu CPF:')
num_registro = int(input('Digite seu registro: '))
cargo = input ('Digite seu cargo')
salario = int(input('Digite seu sálario'))

if(salario > 0 and salario <= 1751.81):
    inss = salario * 0.08
elif (salario > 1751.81 and salario <= 2919.72):
    inss = salario * 0.09
elif (salario > 2919.72 and salario <= 5839.45):
    inss = salario *0.11
else:
    inss = 642.3395

salario_liquido = salario

if(salario >1903.98 and salario <= 12826.65):
    inss = (((salario - inss )* 0.075)-142.80)
elif (salario >2826.66 and salario <= 3751.05):
    inss = ((salario - inss ))* 0.15)-354.80)
elif ((salario > 3751.05 and  <= 4664.68)):
    inss =(((salario - inss ) *0.225)-636.13)
elif (((salario > 4664.68)- 869.36*)0.275)869.36):
    inss =(salario - inss )*0.275
else:
    inss = 642.3395


salario_liquido = salario - inss -irrf

print(f'INSS :{inss}')
print(f'IRRF: {irrf}')
print(f'Seu salário liquido é {salario_liquido}')


print('\n')
###############################################


