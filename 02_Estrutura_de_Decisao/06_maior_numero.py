# 6 - Faça um Programa que leia três números e mostre o maior deles.

numero_1 = float(input('Digite o 1 numero: '))
numero_2 = float(input('Digite o 2 numero: '))
numero_3 = float(input('Digite o 3 numero: '))

if (numero_1 == numero_2) and (numero_1 == numero_3):
    print('Os numeros são iguais.')
elif (numero_1 > numero_2) and (numero_1 > numero_3):
    print(f'O maior numero é {numero_1}')
elif numero_2 > numero_3:
    print(f'O maior numero é {numero_2}')
else:
    print(f'O maior numero é {numero_3}')
