#Desafio049 Tabuada v2.0
# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
valor = int(input('Digite um número para ver sua tabuada:'))
cont = 1
while cont <= 10:
    resultado = cont * valor
    print('{} x {} = {}'.format(cont, valor, resultado))
    cont = cont + 1
