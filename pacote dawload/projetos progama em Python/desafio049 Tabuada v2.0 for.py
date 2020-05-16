#Desafio049 Tabuada v2.0
# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
valor = int(input('Digite um número para ver sua tabuada:'))

for c in range(1, 11):
    resultado = c * valor
    print('{} x {} = {}'.format(c, valor, resultado))
