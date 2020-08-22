"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    a) o produto do dobro do primeiro com metade do segundo .
    b) a soma do triplo do primeiro com o terceiro.
    c) o terceiro elevado ao cubo.
"""
num_int_01 = int(input('Informe um número inteiro: '))
num_int_02 = int(input('Informe outro número inteiro: '))
num_real = float(input('Informe um número real: '))

print(f'O produto do dobro do primeiro com metade do segundo é: {((num_int_01 * 2) + (num_int_02 / 2))}')
print(f'A soma do triplo do primeiro com o terceiro é: {((num_int_01 * 3) + num_real)}')
print(f'O terceiro elevado ao cubo é: {(num_real ** 3)}')
