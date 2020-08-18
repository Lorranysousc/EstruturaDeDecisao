print('3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.\n')

sexo_usuario = str(input('Qual seu sexo? ')).upper()[0] #.upper() vai transformar a entrada do usuário em letra maiúscula e o [0] vai pegar somente a primeira letra caso seja digitado uma palavra.

#Testando possibilidades
if sexo_usuario == 'F':
    sexo_usuario = 'Femino'
elif sexo_usuario == 'M':
    sexo_usuario = 'Masculino'
else:
    sexo_usuario = 'Sexo Inválido'
print(sexo_usuario)
