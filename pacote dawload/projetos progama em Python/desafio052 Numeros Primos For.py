#desafio052 Numeros Primos For
# Faça um progama que leia um número inteiro e diga se ele é ou não um numero primo.
numero = int(input())
cont = total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        cont = cont + 1
if cont == 2:
    print('É primo')
else:
    print('Nao é primo')
print('Ele foi dividido por {} numeros'.format(cont))