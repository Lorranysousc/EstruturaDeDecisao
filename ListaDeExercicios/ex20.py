'''20. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
b. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
c. A mensagem "Aprovado com Distinção", se a média for igual a 10.'''

#Código
from time import sleep

aluno = str(input('Aluno: ')).title()
nota1 = float(input('1ª Nota: '))
nota2 = float(input('2ª Nota: '))
nota3 = float(input('3ª Nota: '))

print(f'{aluno} aguarde! \nEstou calculando sua média...\n')
sleep(3) #Estou pedido que o programa aguarde 3min para exibir a saída.

media = (nota1+nota2+nota3)/3
if media > 10:
    mensagem = 'Valor inválido'
else:
    if media == 10:
        mensagem = 'APROVADO(a) com Distinção'
    elif media >= 7:
        mensagem = 'APROVADO(a)'
    else:
        mensagem = 'REPROVADO(a)'
print(f'{mensagem} com {media:.2f}.')
