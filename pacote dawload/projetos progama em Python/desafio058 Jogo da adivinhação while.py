# desafio058 Jogo da adivinhação while
# Melhore o jogo do desafio 028 onde o computador vai pensar, em um numero entre 0 e 10.
# So que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram
# necessario para vencer.
from random import randint
print('Sou seu computador...')
print('Acabei de pensar em um numero entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
computador = randint(0, 10)
cont = 0
hipotese = False
while hipotese:
    opcao = int(input('Qual a sua opção:'))
    if opcao == computador:
        print('Parabens, você acertou!')
        hipotese = True
    else:
        if opcao > computador:
            print('É menor!')
        else:
            print('É maior!')
    cont = cont + 1
print('Acertou em {} palpites'.format(cont))
