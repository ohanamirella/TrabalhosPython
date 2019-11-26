#--- 3- Crie um programa para calculo de investimento
#--- Solicitar valor a ser investidos no Tesouro Selic (minima 0.01)
#--- (Considerar valor do tesouro Selic Hoje)
#--- Calcular o valor total ate o vencimento do titulo
#--- utilizar metodos


cotas = float(input('Digite a quantidade de cotas : '))

if cotas <= 0.01:
    resultado = cotas * 0.05

else:
    print ('Você não tem a quantidade minima da solicitação de cotas')

print(f'Valor a receber {resultado}')



