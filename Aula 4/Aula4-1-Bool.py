# Aula 4_2 13-11-2019
# Booleanas

#--- Variável booleana simples com True ou False
validador = False
#--- Substituição do valor inicial
validador = True

#--- Criação de variável booleana através de expressão de igualdade
idade = 18
validador = ( idade == 18 )
print(validador)
#--- Criação de variável booleana através de expressão da diferença
validador = ( idade != 18 )
print(validador)
#--- Criação de variável booleana através de expressão de maior
validador = ( idade > 18 )
print(validador)
#--- Criação de variável booleana através de expressão da menor
validador = ( idade < 18 )
print(validador)
#--- Criação de variável booleana através de expressão da maior e igual
validador = ( idade >= 18 )
print(validador)
#--- Criação de variável booleana através de expressão da menor e igual
validador = ( idade <= 18 )
print(validador)

#--- Criação de variável booleana através de expressão de negação
validador = not True
validador = not False

sorteado = 'Marcela'
#--- Criação de variável booleana através de duas expressões e operador E
validador = (sorteado=='Mateus' and sorteado=='Marcela')
#--- Criação de variável booleana através de duas expressões e operador OU
validador = (sorteado=='Mateus' or sorteado=='Marcela')