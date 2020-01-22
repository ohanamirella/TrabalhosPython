#*************************** salvando o arquivo em txt ************

def salvar_aviao(aeroporto):
    arq = open('aviao.txt','w')
    for pessoa in aeroporto:
        arq.write(f'{pessoa}\n')
    arq.close()
#*************************** lendo e salvando em uma lista************
def ler():
    aeroporto1=[]
    arq = open('aviao.txt','r')
    for linha in arq:
        linha = linha.strip()
        aeroporto1.append(linha)      
    arq.close() 
    return aeroporto1  

#*************************** lista das pessoas que estão no aeroporto ************
aeroporto = ['piloto','oficial_A','oficial_B','chefe','comissaria_A',
                            'comissaria_B','policial','presidiario']
aviao = []

#*************************** função que enviara do aeroporto ao avião ************
def viagem ():  

    if len(aeroporto) <= 2:  
        print(f'Viagem ao avião: {aeroporto[0]} e {aeroporto[1]}') 
        aviao.append(aeroporto.pop(0))
        aviao.append(aeroporto.pop(0))
                        
                
    else:
        if aeroporto[1]=='piloto'or aeroporto[1]=='chefe' or aeroporto[1]=='policial':
            aeroporto[0],aeroporto[1]=aeroporto[1],aeroporto[0]
            print(f'Estão no aeroporto: {aeroporto}')
            print(f'Viagem ao avião: {aeroporto[0]} e {aeroporto[1]}')
            aviao.append(aeroporto.pop(1))
                    
        else:
            print(f'Estão no aeroporto: {aeroporto}')
            print(f'Viagem ao avião: {aeroporto[0]} e {aeroporto[1]}')
            aviao.append(aeroporto.pop(1))
                
    if aeroporto:
        print(f'Voltando para aeroporto: {aeroporto[0]}')
        print(f'Dentro do avião {aviao}')
        print('\n') 
    else:
        print(f'Todos no avião {aviao}')  

for i in range(0,7):
    (viagem())
print('\n')
salvar_aviao(aviao)

a=ler()
#*************************** imprimindo o txt ************
print(a)