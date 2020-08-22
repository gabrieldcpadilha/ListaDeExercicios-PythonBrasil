# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# (32 °F − 32) × 5/9 = 0 °C

celsius = float(input('Informe a temperatura em Celsius: '))
farenheit = ((celsius / 5.0) * 9.0) + 32.0
print(f'A temperatura em Farenheit é: {farenheit}')