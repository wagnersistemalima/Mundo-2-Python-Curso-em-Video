#Desafio059 Criando um menu de opções.
# Crie um progama que leia dois valores e mostre um menu como o aõ lado da tela: Seu progama deverá
# realizar a operação solicitada em cada caso.
# [1] somar / [2] multiplicar / [3] maior / [4] novos numeros / [5] sair do progama.
from time import sleep
valor1 = int(input('Primeiro valor:'))
valor2 = int(input('Segundo valor:'))
opcao = 0
while opcao != 5:
    print('-=-'*10)
    print('''Menu!
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do progama''')
    print('-=-'*10)
    opcao = int(input('Qual é sua opção?'))
    if opcao == 1:
        soma = valor1 + valor2
        print('A soma de {} + {} = {}'.format(valor1, valor2, soma))
    elif opcao == 2:
        produto = valor1 * valor2
        print('A multiplicação de {} x {} = {}'.format(valor1, valor2, produto))
    if opcao == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('O maior valor entre o numero {} e {} é {}'.format(valor1, valor2, maior))
    elif opcao == 4:
        print('Informe os números novamente')
        valor1 = int(input('Primeiro valor:'))
        valor2 = int(input('Segundo valor:'))
    if opcao == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção invalida! tente novamete.')

print('Fim do progama! volte sempre.')









