print('7. Faça um Programa que leia três números e mostre o maior e o menor deles.\n')

num1 = float(input('1º número: '))
num2 = float(input('2º número: '))
num3 = float(input('3º número: '))
#Testando possibilidades
if num1 > num2 > num3:
    maior_numero = num1
    menor_numero = num3
elif num1 > num3 > num2:
    maior_numero = num1
    menor_numero = num2
elif num2 > num1 > num3:
    maior_numero = num2
    menor_numero = num3
elif num2 > num3 > num1:
    maior_numero = num2
    menor_numero = num1
elif num3 > num1 > num2:
    maior_numero = num3
    menor_numero = num2
else:
    maior_numero = num3
    menor_numero = num1
print(f'O MAIOR número é o {maior_numero} e o MENOR número é o {menor_numero}.')
