'''4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

entrada_usuario = str(input('Digite uma letra: ')).upper()

tamanho_entrada_usuario = len(entrada_usuario) #Evitar que o usuário digite mais que 1 letra.
if tamanho_entrada_usuario > 1:
    print('Só aceito 1 letra.')
else:
    if entrada_usuario not in 'AEIOU': #Se o que foi digitado pelo usuário (entrada_usuario) não estiver entre as vogais (not in 'AEIOU') o programa vai me retornar que a letra digitada é uma consoante (entrada_usuario = 'CONSOANTE')
        entrada_usuario = 'CONSOANTE'
    else:
        entrada_usuario = 'VOGAL'
    print(entrada_usuario)
