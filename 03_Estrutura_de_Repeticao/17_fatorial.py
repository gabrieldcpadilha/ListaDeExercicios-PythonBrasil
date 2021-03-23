termo = 0

while termo <= 0:
    termo = int(input('Qual termo voce deseja ver o Fatorial? '))
    if termo <= 0:
        print('O termo tem que ser positivo')

fatorial = 1
for n in range(1, termo +1):
    fatorial *= n

print(fatorial)
