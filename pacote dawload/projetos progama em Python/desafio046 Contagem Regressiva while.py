#Desafio 046 . faça um progamaque mostre na tela uma contagem regressiva para o estouro de fogos de
# artificio , indo de 10 ate 0, com uma pausa de 1s entre eles.
from time import sleep
cont = 10
while cont >= 0:
    print(cont)
    cont = cont - 1
    sleep(1)
print('Bumm! Bummmm! Bammmm')

