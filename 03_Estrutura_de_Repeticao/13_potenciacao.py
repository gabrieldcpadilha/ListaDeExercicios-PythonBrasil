base = int(input('Digite o valor da base: '))
expoente = 0

while expoente <= 0:
    expoente = int(input('Digite o valor do expoente: '))
    if expoente <= 0:
        print('O expoente tem que ser positivo')

potencia = 1

for c in range(1, expoente + 1):
    potencia *= base

print(f'{base}^ {expoente} = {potencia}')
