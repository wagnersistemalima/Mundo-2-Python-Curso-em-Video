# desafio068 Jogo do par ou impar While True
# Faça um progama que jogue par ou impar com o computador. o jogo só será interrompido, quando o
# jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no fim do jogo.
from random import randint
cont = 0
while True:
    jogador = int(input('Digite um valor:'))   # Jogador escolhe seu número
    adversario = randint(0, 10)      # adversario escolhe seu numero.
    opcao_jogador = ' '
    soma = jogador + adversario
    while opcao_jogador not in 'PI':
        opcao_jogador = str(input('Par ou Impar? [P/I]').strip().upper()[0])
    if soma % 2 == 0 and opcao_jogador == 'P':
        soma_par = 'PAR'
        print(f'Você jogou {jogador} e o adversario jogou {adversario}. Total de {soma} deu {soma_par}')
        print('Jogador ganhou!')
    elif soma % 2 == 0 and opcao_jogador == 'I':
        soma_par = 'PAR'
        print(f'Você jogou {jogador} e o adversario jogou {adversario}. Total de {soma} deu {soma_par}')
        print('Jogador Perdeu')
        break
    if soma % 2 == 1 and opcao_jogador == 'I':
        soma_impar = 'IMPAR'
        print(f'Você jogou {jogador} e o adversario jogou {adversario}. Total de {soma} deu {soma_impar}')
        print('Jogador ganhou!')
    elif soma % 2 == 1 and opcao_jogador == 'P':
        soma_impar = 'IMPAR'
        print(f'Você jogou {jogador} e o adversario jogou {adversario}. Total de {soma} deu {soma_impar}')
        print('Jogador Perdeu!')
        break
    cont = cont + 1
print(f'GAME OVER! Você venceu {cont} vezes')



