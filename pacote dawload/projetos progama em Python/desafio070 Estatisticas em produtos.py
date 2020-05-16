#desafio070 Estatisticas em produtos
# Crie um progama que leia o nome e o preço de vários produtos. O progama deverá perguntar se o usuario
# vai continuar. No final, mostre:
# A) Qual e o total na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.
from time import sleep
print('{:-^40}'.format('LOJA SUPER BARATÃO'))
status = True
total = cont_preco = menor_preco = produto_maisbarato = 0
cont = 0
while status:
    nome_produto = str(input('Nome do produto:')).strip().upper()
    preco = float(input('preço R$:'))
    opcao = ' '
    total = total + preco
    cont = cont + 1
    while opcao not in 'SN':
        opcao = str(input('Quer continuar [S/N]')).strip().upper()[0]
    if preco > 1000:
        cont_preco = cont_preco + 1
    if cont == 1:
        menor_preco = preco
        produto_maisbarato = nome_produto
    else:
        if preco < menor_preco:
            menor_preco = preco
            produto_maisbarato = nome_produto
    if opcao == 'N':
        status = False
print('{:-^40}'.format('Calculando compras'))
sleep(3)
print(f'Total = R${total:.2f}')     # a)
print(f'{cont_preco} produtos acima de R$ 1000,00')    #b)
print(f'{produto_maisbarato}  custa R${menor_preco:.2f} foi o produto mais barato')
print('{:-^40}'.format('Volte sempre!'))