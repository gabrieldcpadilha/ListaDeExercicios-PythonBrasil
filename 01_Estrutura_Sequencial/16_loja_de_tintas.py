"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

area = float(input('Informe o tamanho da área (metros) a ser pintada: '))

cobertura = area / 3
latas = cobertura / 18

if cobertura % 18 != 0:
    latas += 1

print(f'Quantidade de latas de tinta: {latas}')
print(f'Preço total: R${latas * 80}')
