"""
Faça um programa para o cálculo de uma folha de pagamento,
sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo)
e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
    * Desconto do IR:
    * Salário Bruto até 900 (inclusive) - isento
    * Salário Bruto até 1500 (inclusive) - desconto de 5%
    * Salário Bruto até 2500 (inclusive) - desconto de 10%
    * Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.

       Salário Bruto: (5 * 220)        : R$ 1100,00
       (-) IR (5%)                     : R$   55,00
       (-) INSS ( 10%)                 : R$  110,00
       FGTS (11%)                      : R$  121,00
       Total de descontos              : R$  165,00
       Salário Liquido                 : R$  935,00
"""

# Solicita os dados
valorPorHora = float(input('Informe o valor da hora trabalhada: '))
quantidadeHoras = float(input('Informe a quantidade de horas trabalhadas no mes:'))

# Calcula o salario bruto
salarioBruto = valorPorHora * quantidadeHoras

# Calcula o imposto de renda
if salarioBruto > 2500:
    aliquotaIR = 20
elif salarioBruto > 1500:
    aliquotaIR = 10
elif salarioBruto > 900:
    aliquotaIR = 5
else:
    aliquotaIR = 0

valorIR = salarioBruto * (aliquotaIR / 100.0)

# Calcula o valor para o sindicato
valorSindicato = salarioBruto * (3 / 100.0)

# Calcula o total de descontos
totalDescontos = valorIR + valorSindicato

# Calcula o valor do FGTS
valorFGTS = salarioBruto * (11 / 100.0)

# Calcula o salario liquido
salarioLiquido = salarioBruto - totalDescontos

# Imprime o resultado
print(f'Salario Bruto: {valorPorHora} * {quantidadeHoras}: R$ {salarioBruto}')
print(f'(-) IR {aliquotaIR}%: R$ {valorIR}')
print(f'(-) Sindicato (3%): R$ {valorSindicato}')
print(f'FGTS (11%): R$ {valorFGTS}')
print(f'Total de Descontos: R$ {totalDescontos}')
print(f'Salario Liquido: R$ {salarioLiquido}')
