print('1. Faça um Programa que peça dois números e imprima o maior deles.\n')

num1 = float(input('Digite o 1º número: '))
num2 = float(input('Digite o 2º número: '))

#Testando possibilidades
if num1 > num2:
    print(f'O maior número digitado foi o {num1}.')
elif num2 > num1:
    print(f'O maior número digitado foi o {num2}.')
else:
    print('Os números são iguais.')
