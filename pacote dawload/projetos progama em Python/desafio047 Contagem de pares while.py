#Desafio047 Contagem de Pares.
# Crie um progama que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
cont = 2
while cont <= 50:
    if cont % 2 == 0:
        print(cont, end=' , ')
    cont = cont + 1
print('Fim')
