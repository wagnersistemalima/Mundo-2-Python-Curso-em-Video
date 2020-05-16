# desafio063 Sequencia de Fibonacci v1.0 while
#Escreva um progama que leia um número n inteiro qualquer e mostre na tela os n primeiros
# elementos de uma Sequência de Fibonacci. EX: 0 - 1 - 1 - 2 - 3 - 5 - 8
# Dica Fibonacci -> soma do anterior com sucessor            t1 + t2 = t3
quant_termos = int(input('Quantos termos você quer mostrar: '))
termo1 = 0            # O primeiro termo Sempre vai ser 0
termo2 = 1            # O segundo termo sempre vai ser 1
print('{} -> {}'.format(termo1, termo2), end=' ')  # A partir do terceiro termo, vejamos algumas condiçoes
cont = 3
while cont <= quant_termos:
    termo3 = termo1 + termo2
    print('-> {}'.format(termo3), end=' ')
    termo1 = termo2                           # Atualizar o termo 1
    termo2 = termo3                           # Atualizar o termo 2
    cont = cont + 1
print('Fim!')




