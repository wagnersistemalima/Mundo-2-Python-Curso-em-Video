#desafio055 Maior e menor da sequência
# Faça um progama que leia o peso de cinco pessoas. No final, mostre qual foi o
# maior e o menor pesos lidos.
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}º pessoa:'.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
