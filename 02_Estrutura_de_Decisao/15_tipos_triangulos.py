"""
Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
"""

lado1 = float(input('Informe o valor do Lado 1: '))
lado2 = float(input('Informe o valor do Lado 2: '))
lado3 = float(input('Informe o valor do Lado 3: '))

# Verifica se eh um triangulo
if (lado1 > (lado2 + lado3)) or (lado2 > (lado1 + lado3)) or (lado3 > (lado1 + lado2)):
    triangulo = False
else:
    triangulo = True

if triangulo:
    print('Os valores formam um Triangulo')

    # Verifica o tipo de triangulo
    if (lado1 == lado2) and (lado2 == lado3):
        print('Triangulo Equilatero')
    elif (lado1 == lado2) or (lado1 == lado2) or (lado2 == lado3):
        print('Triangulo Isosceles')
    else:
        print('Triangulo Escaleno')
else:
    print('Os valores não formam um triangulo')
