'''10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''


turno = str(input(f'Olá! \nEm que turno você estuda? \n[M]matutino [V]vespertino [N]noturno\n')).upper()[0] #.upper() vai transformar a entrada do usuário em letra maiúscula e o [0] vai pegar somente a primeira letra caso seja digitado uma palavra.
if turno not in 'MVN':
    print('Valor inválido!')
else:
    if turno == 'M':
        mensagem = 'Bom Dia!'
    elif turno == 'V':
        mensagem = 'Boa Tarde!'
    else:
        mensagem = 'Boa Noite!'
    print(mensagem)
