num = 0
while num <= 0:
    num = int(input('Voce quer ver qual numero se é primo? '))
    if num <= 0:
        print('O numero deve ser positivo')

primo = True
for i in range(2, (num / 2 + 1)):
    if num % i == 0:
        primo = False
        break

if primo:
    print('O numero é primo')
else:
    print('O numero nao é primo')
    print('Ele é divisivel por: ')
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end='')
