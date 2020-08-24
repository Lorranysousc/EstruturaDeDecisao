'''12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
- Salário Bruto até 900 (inclusive) - isento
- Salário Bruto até 1500 (inclusive) - desconto de 5%
- Salário Bruto até 2500 (inclusive) - desconto de 10%
- Salário Bruto acima de 2500 - desconto de 20% '''

#Código
horas_mes = int(input('Horas trabalhadas por mês: '))
valor_hora = float(input('Valor hora R$'))
salario_bruto = horas_mes*valor_hora

#Descontos
sindicato = (salario_bruto*3)/100
inss = (salario_bruto*10)/100
#Cálculo IR
if salario_bruto <= 900:
    ir = 0
    valor_ir = 0
elif 900 < salario_bruto <= 1500:
    ir = 5
    valor_ir = (salario_bruto*ir)/100
elif 1500 < salario_bruto <= 2500:
    ir = 10
    valor_ir = (salario_bruto*ir)/100
else:
    ir = 20
    valor_ir = (salario_bruto*ir)/100
print('**FOLHA DE PAGAMENTO**')
print(f'''
Salário Bruto          : R$ {salario_bruto:.2f}
(-) IR ({ir}%)            : R$ {valor_ir:.2f}
(-) Sindicato (3%)     : R$ {sindicato:.2f}
(-) INSS (10%)         : R$ {inss:.2f}
FGTS (11%)             : R$ {(salario_bruto*11)/100:.2f}
Total de descontos     : R$ {valor_ir + sindicato + inss:.2f}
Salário Liquido        : R$ {salario_bruto - valor_ir - sindicato - inss:.2f}''') #:.2f é uma formatação para que o programa imprima o valor(float) com 2 casas após a vírgula.
