# Desafio065 Maior e Menor valores while.
# Crie um progama que leia varios números inteiros pelo teclado. no final da execução, mostre a media
# entre todos os valores e qual foi o maior e o menor valores lidos. o progama deve perguntar ao usuario
# se ele quer ou não continuar a digitar valores.
opcao = 'S'
soma = quant = media = menor = maior = 0
while opcao == 'S':
    valor = int(input('Digite um valor:'))
    opcao = str(input('Quer continuar:[S] / [N}:').strip().upper()[0])
    soma = soma + valor
    quant = quant + 1
    if quant == 1:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))









