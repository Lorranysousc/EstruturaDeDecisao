print('2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.\n')

entrada_usuario = float(input('Digite um número: '))

#Testando possibilidades
if entrada_usuario >= 0:
    valor = 'POSITIVO'
else:
    valor = 'NEGATIVO'
print(f'O número digitado é {valor}.')