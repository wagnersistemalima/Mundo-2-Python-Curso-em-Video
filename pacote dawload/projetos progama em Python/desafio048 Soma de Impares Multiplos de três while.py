#Desafio048 faça um progama que calcule a soma entre todos os números impares que são múltiplos
# de três e que se encontram no intervalo de 1 até 500.
cont = 1
soma = 0
contador = 0
while cont <= 500:
    if cont % 2 == 1 and cont % 3 == 0:
        contador = contador + 1
        soma = soma + cont

    cont = cont + 1
print('A soma de todos os {} números solicitados é {}.'.format(contador, soma))

