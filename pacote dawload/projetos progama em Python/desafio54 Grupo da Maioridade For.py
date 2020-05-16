# Desafio054 grupo da maioridade.
#Crie um progama que leia o ano de nascimento de sete pessoas. no final, mostre quantas pessoas
# ainda não atigiram a maioridade e quantas já são maiores.
from datetime import date
ano_atual = date.today().year
cont = 0
cont_maior = 0
for c in range(1, 8):
    ano = int(input('Digite o {} ano de nascimento de uma pessoa:'.format(c)))
    maioridade = ano_atual - ano
    if maioridade < 21:
        cont = cont + 1
    else:
        cont_maior = cont_maior + 1

print('{} pessoas são de menores'.format(cont))
print('{} pessoas atigiram a maioridade'.format(cont_maior))


