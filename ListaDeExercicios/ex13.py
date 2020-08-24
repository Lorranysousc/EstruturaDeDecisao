'''13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''

#Código
print('Escolha um Número entre 1 e 6 e veja o Dia da semana correspondente:')
entrada_usuario = int(input('Número '))
if entrada_usuario == 1:
    dia_da_semana = 'Domingo'
elif entrada_usuario == 2:
    dia_da_semana = 'Segunda-feira'
elif entrada_usuario == 3:
    dia_da_semana = 'Terça-feira'
elif entrada_usuario == 4:
    dia_da_semana = 'Quarta-feira'
elif entrada_usuario == 5:
    dia_da_semana = 'Quinta-feira'
elif entrada_usuario == 6:
    dia_da_semana = 'Sexta-feira'
else:
    dia_da_semana = 'Valor inválido'
print(dia_da_semana)
