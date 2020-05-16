#Desafio048 faça um progama que calcule a soma entre todos os números impares que são múltiplos
# de três e que se encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os {} números solicitados é {}.'.format(cont, soma))

