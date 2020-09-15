# 08 - Faça um programa que pergunte o preço de três produtos e
# informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato

preco1 = int(input('Informe o primeiro preco: '))
preco2 = int(input('Informe o segundo preco: '))
preco3 = int(input('Informe o terceiro preco: '))

if preco1 == preco2 and preco1 == preco3:
    print('Compre por qualquer um. Os precos sao iguais.')
elif preco1 < preco2 and preco1 < preco3:
    print(f'Compre pelo primeiro preco {preco1}')
elif preco2 < preco3:
    print(f'Compre pelo segundo preco {preco2}')
else:
    print(f'Compre pelo terceiro preco {preco3}')
