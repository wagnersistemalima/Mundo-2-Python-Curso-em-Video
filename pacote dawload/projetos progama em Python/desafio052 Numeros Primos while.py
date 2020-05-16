#desafio052 Numeros Primos while
# Faça um progama que leia um número inteiro e diga se ele é ou não um numero primo.
casos = int(input('Quantos casos você ira verificar?'))
cont = 1
contador = 0
contador_casos = 1
while contador_casos <= casos:
    numero = int(input('Digite um número:'))
    while cont <= numero:
        if numero % cont == 0:
            contador = contador + 1
        cont = cont + 1
    if contador == 2:
        print('É primo')
    else:
        print('Não é primo')
    contador_casos = contador_casos + 1