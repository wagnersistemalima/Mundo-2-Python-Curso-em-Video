#Desafio047 Contagem de Pares.
# Crie um progama que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
for c in range(2, 51):
    if c % 2 == 0:
        print(c, end=' , ')
print('Fim')
