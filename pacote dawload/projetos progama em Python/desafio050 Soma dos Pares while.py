# desafio050 Soma dos Pares While
#Desenvolva um progama que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares. se o
# valor for impar, desconsidere-o.
cont = 1
acumulador = contador = 0
while cont <= 6:
    valor = int(input('Digite o {} número:'.format(cont)))
    if valor % 2 == 0:
        acumulador = acumulador + valor
        contador = contador + 1
    cont = cont + 1
print('Você informou {} numeros pares, e a soma entre eles é {}'.format(contador, acumulador))

