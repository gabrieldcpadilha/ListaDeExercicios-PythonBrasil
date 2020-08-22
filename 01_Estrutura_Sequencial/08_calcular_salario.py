"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""
salario_hora = float(input('Informe seu salário por hora trabalhada: '))
qtd_horas = float(input('Informe sua quantidade de horas trabalhadas no mês: '))

total = salario_hora * qtd_horas

print(f'O total do salário referido no mês foi: R${total}')
