#desafio055 Maior e menor da sequência
# Faça um progama que leia o peso de cinco pessoas. No final, mostre qual foi o
# maior e o menor pesos lidos.
cont = 1
maior = 0
menor = 0
while cont <= 5:
    peso = int(input('Digite o peso da {}º pessoa:'.format(cont)))
    if cont == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    cont = cont + 1
print('O maior peso digitado foi {}Kg'.format(maior))
print('O menor peso digitado foi {}Kg'.format(menor))


