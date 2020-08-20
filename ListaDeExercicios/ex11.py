'''11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante : aumento de 5% 

Após o aumento ser realizado, informe na tela:
- o salário antes do reajuste;
- o percentual de aumento aplicado;
- o valor do aumento;
- o novo salário, após o aumento.'''

#Código
salario_inicial = float(input('Salário Inicial R$'))

if salario_inicial <= 280:
    percentual = 20
    valor_aumento = (salario_inicial*percentual)/100
    novo_salario = salario_inicial+valor_aumento
elif 280 < salario_inicial <= 700:
    percentual = 15
    valor_aumento = (salario_inicial*percentual)/100
    novo_salario = salario_inicial+valor_aumento
elif 700 < salario_inicial <= 1500:
    percentual = 10
    valor_aumento = (salario_inicial*percentual)/100
    novo_salario = salario_inicial+valor_aumento
else:
    percentual = 5
    valor_aumento = (salario_inicial*percentual)/100
    novo_salario = salario_inicial+valor_aumento
print(f'''
Salário inicial: R$ {salario_inicial:.2f}
Percentual de aumento: {percentual}%
Valor do aumento: R$ {valor_aumento:.2f}
Novo Salário: R$ {novo_salario:.2f} ''')
