"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
"""
h = float(input('Informe sua altura (em metros): '))
sexo = input('Informe seu sexo (M = Mulher / H = Homem) :')

if sexo == 'H' or sexo == 'h':
    peso_ideal = (72.7 * h) - 58
    print(f'O seu peso ideal é: {peso_ideal}')
elif sexo == 'M' or sexo == 'm':
    peso_ideal = (65.1 * h) - 44.7
    print(f'O seu peso ideal é: {peso_ideal}')
else:
    print('Opção inválida.')
