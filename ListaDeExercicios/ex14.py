'''14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:'''


#Entrada usuário
aluno = str(input('Aluno: ')).title() #.title() transforma em maiúscula a primeira letra de cada palavra, tendo como norte os espaços.
disciplina = str(input('Disciplina: ')).title()
nota1 = float(input('1ª Nota: '))
nota2 = float(input('2ª Nota: '))

#Conceito
media = (nota1 + nota2)/2
if media > 10:
    print('Valor inválido')
    exit() #Finaliza o programa caso a média > 10
else:
    if 9 <= media <= 10:
        conceito = 'A'
    elif 7.5 <= media < 9:
        conceito = 'B'
    elif 6 <= media < 7.5:
        conceito = 'C'
    elif 4 <= media < 6:
        conceito = 'D'
    else:
        conceito = 'E'
#Mensagem
if conceito in 'ABC':
    mensagem = 'APROVADO'
else:
    mensagem = 'REPROVADO'
print(f'''
Disciplina: {disciplina}
1ª Nota: {nota1}
2ª Nota: {nota2}
Média: {media}
Conceito: {conceito}
{aluno} você foi {mensagem}(a)!''')    
