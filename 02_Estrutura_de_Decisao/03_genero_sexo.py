# 3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

genero = str(input('Escolha um genero ("F" Feminino / "M" Masculino): '))

if genero in 'mM':
    print(f'O genero escolhido é {genero} - Masculino')
elif genero in 'fF':
    print(f'Seu genero é {genero} - Feminino')
else:
    print(f'Você selecionou uma opção invalida: ({genero})')
