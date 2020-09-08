'''15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
- Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
- Triângulo Equilátero: três lados iguais;
- Triângulo Isósceles: quaisquer dois lados iguais;
- Triângulo Escaleno: três lados diferentes;'''

lado1 = float(input('Lado 1: '))
lado2 = float(input('Lado 2: '))
lado3 = float(input('Lado 3: '))

#Testando se é triângulo
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    #Tipo de triângulo
    if lado1 == lado2 == lado3:
        tipo_triangulo = 'Equilátero'
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        tipo_triangulo = 'Isósceles'
    elif lado1 != lado2 != lado3:
        tipo_triangulo = 'Escaleno'
    print(f'Triângulo {tipo_triangulo}')
else:
    print('Não é um triângulo')
