# Desafio054 grupo da maioridade.
#Crie um progama que leia o ano de nascimento de sete pessoas. no final, mostre quantas pessoas
# ainda não atigiram a maioridade e quantas já são maiores.
from datetime import  date
casos = 1
cont_menor = 0
cont_maior = 0
ano_atual = date.today().year
while casos <= 7:
    ano = int(input('Digite o ano de nascimento da pessoa {}:'.format(casos)))
    casos = casos + 1
    if ano_atual - ano < 21:
        cont_menor = cont_menor + 1
    else:
        cont_maior = cont_maior + 1
print('{} pessoa(s) são de menor'.format(cont_menor))
print('{} pessoa(s) são de maior'.format(cont_maior))


