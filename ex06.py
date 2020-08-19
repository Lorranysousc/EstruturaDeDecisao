print('6. Faça um Programa que leia três números e mostre o maior deles.\n')

num1 = float(input('1º número: '))
num2 = float(input('2º número: '))
num3 = float(input('3º número: '))
#Testando possibilidades
if num2 < num1 > num3:
    maior_numero = num1
elif num1 < num2 > num3:
    maior_numero = num2
else:
    maior_numero = num3
print(f'O maior número é o {maior_numero}.')
