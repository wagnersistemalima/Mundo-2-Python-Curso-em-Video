# desafio064 Tratando varios valores v1.0 while
# Crie um progama que leia varios números inteiros pelo teclado. o progama só vai parar quado o
# Usuario digitar 999, que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles(Desconsiderando o flag)
condicao = 999
cont = soma = 0
numero = int(input('Digite um número:[999 para parar]: ')) # para eliminar o numero 999 da soma. ler antes
while numero != condicao:
    soma = soma + numero
    cont = cont + 1
    numero = int(input('Digite um número:[999 para parar]: '))     # e depois ler no fim do laço:
print('Foram digitados {} numeros e a soma entre eles foi de {}'.format(cont, soma))
