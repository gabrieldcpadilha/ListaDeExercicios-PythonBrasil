"""
Faça um Programa que peça a temperatura em graus Fahrenheit,
transforme e mostre a temperatura em graus Celsius.

C = 5 * ((F-32) / 9).
"""

farenheit = float(input('Informe a temperatura em Farenheit: '))
celsius = 5 * (farenheit - 32) / 9.0
print(f'A temperatura em Celsius é: {celsius}')
