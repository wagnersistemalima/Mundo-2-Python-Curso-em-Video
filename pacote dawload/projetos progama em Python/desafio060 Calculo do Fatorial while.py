#desafio060 calculo de fatorial
# Faça um progama que leia um número qualquer e mostre o seu fatorial.
# EX; 5! = 5 x 4 x 3 x 2 x 1 = 120
numero = int(input('Digite um numero para calcular seu fatorial:'))
cont = numero
acumulador = 1
print('calculando {}! ='.format(cont), end=' ')
while cont > 0:
    print(cont, end=' ')
    print('x' if cont > 1 else '', end=' ')
    acumulador = acumulador * cont
    cont = cont - 1
print('= {} Fim!'.format(acumulador))
