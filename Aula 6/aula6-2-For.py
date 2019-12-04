# Aula 6 - P2 - 13-11-2019
# Estruturas de repetição - FOR

#--- For simples usando range com incremento padrão de 1
for i in range(0,10):
    print(f'{i}- Padawans HbPy')

#--- For usando range com incremento de 2
for i in range(0,100,2):
    print(f'{i}- Pares')

#--- For em lista usando range
lista = ['Mateus','Matheus','Marcela','Nicole','Tonho','Pablo']
for i in range(0,6):
    print(lista[i])

#--- Exemplificando o problema do uso de For em lista usando range
lista.append('Natan')
for sortudo in lista:
    print(sortudo)

#--- For usando os elementos da própria lista (foreach)
numero = 10
for i in range(0,11):
    print(f'{i} x {numero} = {i*numero} ')