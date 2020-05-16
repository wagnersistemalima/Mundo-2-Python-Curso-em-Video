# desafio 45. Crie um progama que faça o computador jogar jokenpô com você.
from time import sleep # importar um tempo pra fazer o computador dizer  jo kem po. com pauuza tempo
from random import randint # funçao importar , escolher numeros aleatorios
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2) # escolher numeros de 0 a 2
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
sleep(1)
print('-='*10)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*10)
if computador == 0: # Computador jogou Pedra
    if jogador == 0:
      print('Empate')
    elif jogador == 1: # Jogador jogou Papel
      print('Jogador Vence')
    elif jogador == 2: # jogador jogou Tesoura
      print('Jogador Perde')
    else:
        print('Jogada invalida!')
elif computador == 1: # Computador jogou papel
    if jogador == 0: # jogador jogou pedra
        print('Computador vence')
    elif jogador == 1: # jogador jogou papel
        print('Empate')
    elif jogador == 2: # Jogador jogou Tesoura
        print('Jogador vence')
    else:
        print('Jogada invalida!')
elif computador == 2: # Computador jogou Tesoura
    if jogador == 0: # Jogador jogou Pedra
        print('Jogador vence')
    elif jogador == 1: # jogador jogou papel
        print('Computador vence')
    elif jogador == 2: # Jogador jogou tesoura
        print('Empate')
    else:
        print('Jogada invalida!')