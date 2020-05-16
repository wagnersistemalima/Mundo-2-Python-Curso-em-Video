#desafio060 calculo de fatorial
# # Faça um progama que leia um número qualquer e mostre o seu fatorial.
# # EX; 5! = 5 x 4 x 3 x 2 x 1 = 120
numero = int(input('Digite um número para calcular seu fatorial:'))
print('Calculando {}! ='.format(numero), end=' ')
acumulador = 1
for c in range(numero, 0, -1):
    acumulador = acumulador * c
    print(c, end=' ')
    print('x' if c > 1 else ' ', end=' ')
print('= {} Fim!'.format(acumulador), end='')