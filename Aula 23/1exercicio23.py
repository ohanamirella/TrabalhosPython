# Aula 22 - 10-12-2019
# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:

dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

# 1) Faça uma classe cliente que receba como parametro o dado bruto.
# 2) A classe deve iniciar (__init__) guardando o dado bruto nume variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None
# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)



class Pessoa:
    def __init__ (self,dadobruto):
        self.dado_bruto = dadobruto
        self.codigo = None
        self.nome = None
        self.idade = None
        self.sexo = None
        self.email = None
        self.telefone = None
    
    def tratar_dados(self):
        pessoa = self.dado_bruto.strip().split(';')
        self.codigo = int( pessoa[0] )
        self.nome = pessoa[1]
        self.idade = int( pessoa[2] )
        self.sexo = pessoa[3]
        self.email = pessoa[4]
        self.telefone = pessoa [5]
        

    def salvar (self):
        alquivo = open('Aula23/resolução/salvarciente.txt','a')
        texto = 
        '''
        o __str__ é uma sobrecarda de operador que irá retornar um texto 
        Assim quando você printar sua classe, irá aparecer o seu texto.
        Note que foi colocado o texto dentro de uma doc string (três aspas)
        e isso deu a liberdade para colocar o texto fora de identação.
        necessita do return para retornar o texto
        '''
        texto = f'''
Codigo: {self.codigo}
Nome: {self.nome}
Idade: {self.idade}
Sexo: {self.sexo }
E-mail: {self.email} 
Telefone: {self.telefone}'''

        return texto


    def __eq__(self,valor):
        '''
        Este comando (sobrecarga de operadores para o igual ==) ele 
        habilita a classe poder fazer operações de igualdade (==) sem
        chamar a variável.
        Ela necessita que passar uma variável por parametro. (valor) que 
        será trabalhada dentro do metodo.
        Necessita do return para retornar o resultado da operação.
        Nota-se que estou querendo comparar o código do cliente. mas poderia
        testar qualquer variável necessitando apenas trocar o self.codigo pelo
        sel. com o atributo (variável) de sua preferência
        '''


        return self.codigo == valor
        # este return irá retornar verdadeiro (True) ou falso (False)
         

dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

# Como a classe é atribuida para uma variável e esta possui o dado de uma
# só pessoa, surge a necessidade de criar várias variáveis para guardar 
# várias pessoas. 
# A melhor forma de salvar várias pessoas é usar uma lista e adicionar-la
# via metodo .append()

pess = [] 
pess.append( Pessoa(dadobruto) ) #criando um cliente dentro da lista

#Chamando a ação (metodo) tratar_dados que irá pegar o dado
#bruto e atribuir nos atributos do cliente
pess[0].tratar_dados() 


# Testando para ver se os dados foram atribuidos de forma correta!
print(f'Codigo: {pess[0].codigo+1}\nNome: {pess[0].nome}')


# Se lembra do metodo criado lá em cima ( __str__ )... Então este metodo 
# habilitou para mostrar os dados quando chamado com o o print
print(pess[0])



while True:
    var = int(input('Digite o código cliente: '))

    # se lembra do metodo __eq__, ele habilitou a classe para poder fazer
    # operações com o igual == . 
    print( pess[0] == var )
def salvar (self):
    try:
        arquivo = open ('23-Aula23/exercicios/')
        for pessoa in self.lista:
            texto = f'{pessoa['pessoa']}'

