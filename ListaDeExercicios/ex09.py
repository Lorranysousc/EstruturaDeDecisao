'''9. Faça um Programa que leia três números e mostre-os em ordem decrescente.'''

num1 = float(input('1º Número: '))
num2 = float(input('2º Número: '))
num3 = float(input('3º Número: '))

if num3 > num2:
    num_auxiliar = num3 #Estou usando a variável 'num_auxiliar' porque o num3 é minha referência. Caso eu não declare essa variável, quando eu definir que num3 é maior que o num2 e por isso, o num2 passa a ser o num3, o print vai trazer 2 números repetidos.
    num3 = num2
    num2 = num_auxiliar

if num2 > num1:
    num_auxiliar = num2
    num2 = num1
    num1 = num_auxiliar

if num3 > num2:
    num_auxiliar = num3
    num3 = num2
    num2 = num_auxiliar
print(f'{num1}, {num2}, {num3}')
