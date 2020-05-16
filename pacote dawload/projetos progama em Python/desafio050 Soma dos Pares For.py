# desafio050 Soma dos Pares For
#Desenvolva um progama que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares. se o
# valor for impar, desconsidere-o.
acumulador = cont = 0
for c in range(1, 7):
    valor = int(input("Digite o {} número:".format(c)))
    if valor % 2 == 0:
        acumulador = acumulador + valor
        cont = cont + 1
print('Você informou {} números pares e a soma entre eles é {}'.format(cont, acumulador))
