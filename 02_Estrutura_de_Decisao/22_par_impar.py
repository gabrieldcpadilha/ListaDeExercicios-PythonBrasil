# Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão).


valor = int(input('Informe um numero: '))

if valor % 2 == 0:
    print(f'O valor {valor}: é PAR')
else:
    print(f'O valor {valor}: é IMPAR')
