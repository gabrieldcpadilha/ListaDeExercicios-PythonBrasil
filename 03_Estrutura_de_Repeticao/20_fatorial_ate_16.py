qtd = 0
while qtd <= 0:
    qtd = int(input('Voce quer a fatorial de quantos numeros? '))
    if qtd <= 0:
        print('Quantidade deve ser positiva')

for i in range(0, qtd):
    termo = 0
    while termo <= 0 or termo > 16:
        termo = int(input('Voce quer o fatorial de qual termo? '))
        if termo <= 0:
            print('O termo deve ser positivo')
        if termo > 16:
            print('O termo deve ser menor que 16')

    fatorial = 1
    for i in range(1, termo + 1):
        fatorial *= i

    print(fatorial)
