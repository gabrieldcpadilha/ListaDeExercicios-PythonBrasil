"""Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

tamanho = float(input('Informe o tamanho do arquivo (em MB): '))
velocidade = float(input('Informe a velocidade de conexao (em Mbps): '))

tamanhoBits = tamanho * 1024 * 1024 * 8
tempoSegundos = tamanhoBits / (velocidade * 1024 * 1024)
tempoMinutos = tempoSegundos / 60

print(f'O Tempo de download aproximado foi de: {tempoMinutos} minutos')
