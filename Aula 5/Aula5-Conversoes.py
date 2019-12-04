# Crie um programa que leia 4 notas
# Imprima a maior nota
# Imprima a menor nota
# Imprima a média
# Imprima se o aluno foi aprovado ou reprovado (Media 7.0)

nota=int(input('Digite a primeira nota: '))
nota2=int(input('Digite a segunda nota: '))
nota3=int(input('Digite a terceira nota: '))
nota4=int(input('Digite a quarta nota: '))

# lista = [nota, nota2, nota3, nota4]
# print("A maior nota foi:", max(lista))

# lista = [nota, nota2, nota3, nota4]
# print("A menor nota foi:", min(lista))

if nota<nota2 and nota<nota3 and nota<nota4:
    print(f'A menor nota é a primeira. ({nota})')
elif nota2<nota and nota2<nota3 and nota2<nota4:
    print(f'A menor nota é a segunda. ({nota2})')
elif nota3<nota and nota3<nota2 and nota3<nota4:
    print(f'A menor nota é a terceira. ({nota3})')
else:
    print(f'A menor nota é a quarta. ({nota4})')


if nota>nota2 and nota>nota3 and nota>nota4:
    print(f'A maior nota é a primeira. ({nota})')
elif nota2>nota and nota2>nota3 and nota2>nota4:
    print(f'A maior nota é a segunda. ({nota2})')
elif nota3>nota and nota3>nota2 and nota3>nota4:
    print(f'A maior nota é a terceira. ({nota3})')
elif nota4>nota and nota4>nota3 and nota4>nota2:
    print(f'A maior nota é a quarta. ({nota4})')

media = (nota + nota2 + nota3 + nota4) / 4

print(f'media = {media}')

if media >= 7:
    print('Aprovado')
else:
    print('Reprovado')