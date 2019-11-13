nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segundo nota: '))
nota3 = float(input('Digite a tereiro nota: '))
nota4 = float(input('Digite a quarta nota: '))

if nota1 > nota2 and nota1  > nota3 and nota1 > nota4:
    print (f'Nota {nota1} é a maior nota')
elif nota2 > nota1 and nota2 > nota3 and nota2 > nota4:
    print (f'Nota {nota2} é maior nota')
elif nota3 > nota1 and nota3 > nota2 and nota3 > nota4:
    print(f'Nota {nota3} é maior nota')
elif nota4 > nota1 and nota4 > nota2 and nota4 > nota3:
    print(f'Nota {nota4} é maior nota')
if nota1 < nota2 and nota1 < nota3 and nota1 < nota4:
    print (f'Nota {nota1} é a menor nota')
elif nota2 < nota1 and nota2 < nota3 and nota2 < nota4:
    print(f'Nota {nota2} é a menor nota')
elif nota3 < nota1 and nota3 < nota2 and nota3 < nota4:
    print (f'Nota {nota3} é a menor nota')
elif nota4 < nota1 and nota4 < nota2 and nota4 < nota3:
    print (f'Nota {nota4} é a menor nota')
else:
	print(f'As notas são iguais {nota1} , {nota2} , {nota3} e {nota4} ')

media = (nota1 + nota2 + nota3 + nota4) / 4
print (f'{media}')

if media >= 7:
    print('Aluno aprovado')
else :
    print('Aluno reprovado')

