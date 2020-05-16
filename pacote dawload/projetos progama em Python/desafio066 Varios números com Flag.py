# desafio066 Varios números com Flag
# Crie um progama que leia vários números inteiros pelo teclado. o progama só vai parar quando o
# usuario digitar o valor 999, que é a condição de parada. No final mostre quantos números foram
# digitados e qual foi a soma entre eles. (Desconsiderando o flag)
validacao = False
soma = cont = 0
while not validacao:
    numero = int(input('Digite um valor:'))
    if numero == 999:
        validacao = True
    elif numero != 999:
        soma = soma + numero
        cont = cont + 1
print(f'Foram digitados {cont} valores e a soma entre eles é {soma}')
