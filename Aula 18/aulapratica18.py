# Aula 18 - 03-11-2019
# Exercicios para lista simples


# Dada a seguinte lista, resolva os seguintes questões:

lista = ["10", "20", "amor", "abacaxi", "80", "Abioluz", "Cachorro grande é de arrasar"]

#print('1: Usando a indexação, escreva na tela a palavra abacaxi')
print(lista[3])

#print('2: Usando a indexação, escreva na tela os seguintes dados: 20, amor, abacaxi')
print(lista[1:4])

#print('3: Usando a indexação, escreva na tela uma lista com dados de 20 até Abioluz')
print(lista[1:6])

#print('4: Usando a indexação, escreva na tela uma lista com os seguintes dados:'
#     '\nCachorro grande é de arrasar, Abioluz, 80, abacaxi, amor, 20, 10')
print(lista[::-1])

#print('5: Usando o f-string e a indexação escreva na tela os seguintes dados:'
#      '\n { abacaxi } é muito bom, sinto muito { amor } quando eu chupo { 80 }" deles.')

#print('6: Usando a indexação, escreva na tela os seguintes dados:'
#      '\n10, amor, 80, Cachorro grande é de arrasar')
#lista = [0,2,3,4,6]
print(lista[0]),print(lista[2]),print(lista[3]),print(lista[4]),print(lista[6])

#print('7: Usando o f-string e a indexação escreva na tela os seguintes dados:'
#      'Abioluz - abacaxi - 10 - Cachorro grande é de arrasar - 20 - 80' )
#print(lista[6,4,0,7,2,5])
print(lista[6]),print(lista[4]),print(lista[0]),print(lista[2]),print(lista[5])

#print('8: Usando o f-string e a indexação escreva na tela os seguintes dados:'
#      '\namor - 10 - 10 - abacaxi - Cachorro grande é de arrasar - Abioluz - 10 - 20')


#print('9: Usando a indexação, escreva na tela uma lista com dados de 10 até 80')
#print(lista[0:4])
#print('10: Usando a indexação, escreva na tela os seguintes dados:'
#     '\n10, abacaxi, Cachorro grande é de arrasar')
#print(lista[0,3,7])

############################################################

# Aula 18 - 03-11-2019
# Exercicio para lista dentro de lista

# Dada a seguinte lista, resolva os seguintes questões:

lista = [
          ['frutas','verduras','legumes'],
          ['mamão','abacaxi','laranja','uva','pera','maçã','vergamota'],
          ['alface crespa', 'alface lisa','rucula','almerão','repolho','salsinha',],
          ['feijão', 'erviha', 'lentilha','vagem','feijão branco','gão de bico','soja']
        ]

# A lista está organizada da seguinte forma:
#       A primeira lista é o cabeçalho que diz o que siguinifica cada lista a seguir. Ex: Lista de frutas, lita de verduras
#       lista de legumes.
# Com isso responda as seguintes questões:


print('1: imprima a lista cabeçalho e mostre todos os seus elemantos')

print('2: imprima a lista verduras e mostre todos os seus elemantos')

print('3: imprima com f-string a seguinte sequência: abacaxi - laranja - maçã - vergamota')

print('4: imprima com f-string a seguinte sequência: alface lisa - salsinha - rucula - alface crespa')

print('5: imprima com f-string a seguinte sequência: frutas: laranja e prera - verduras: repolho e rucula'
      '\nlegumes: ervilha, feijão branco e grão de bico')

print('6: imprima com f-string a seguinte sequência: mamão - ervilha, rucula, salsinha, mamão, repolho')

print('7: imprima com f-string a seguinte sequência: fruta: 3kg de laranja, 8kg de uva, 4.5kg de maçã, 1kg de vergamota')

print('8: imprima com f-string a seguinte sequência: verduras: 5 maço de salsinha, 4 pés de alface crespa e alface lisa'
      '2 cabeças de repolho')

print('9: imprima com f-string a seguinte sequência: legumes: 1kg de feijão, 2kg de gão de bico, 1.5 kg dde soja,'
      '1 pacote de ervilha')

print('10: imprima a lista legumes e mostre todos os seus elemantos')