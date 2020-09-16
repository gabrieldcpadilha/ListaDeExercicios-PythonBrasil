"""Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

    1 - par ou ímpar;
    2 - positivo ou negativo;
    3 - inteiro ou decimal.
"""

numero = float(input('Informe um numero: '))

print(' 1 - Par ou Impar')
print(' 2 - Positivo ou Negativo')
print(' 3 - Inteiro ou Decimal')
opcao = input('>> Escolha uma opção: ')

if opcao == '1':
    if numero % 2 == 0:
        print('O número é par')
    else:
        print('O número é impar')
elif opcao == '2':
    if numero < 0:
        print('O número é negativo')
    elif numero > 0:
        print('O número é positivo')
    else:
        print('O número é igual a zero')
elif opcao == '3':
    if numero == int(numero):
        print('O número é inteiro')
    else:
        print('O número é decimal')
else:
    print('Opção Inválida')
