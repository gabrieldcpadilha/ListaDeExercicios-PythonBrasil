num = int(input('Informe o numero que voce deseja ver a tabuada: '))

print(f'Tabuada de {num}')
for c in range(0, 11):
    print(f'{num} X {c} = {num * c}')
