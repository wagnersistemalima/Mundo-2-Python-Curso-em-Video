#Desafio061 Progressão Aritimetica.
#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
# termos dessa progressão.
print('Gerador de PA')
print('-=-'*10)
termo = int(input('Primeiro termo:'))     # inicio
razao = int(input('Razão:'))     # passo
cont = 1
while cont <= 10:
    print(termo, end=' , ')
    termo = termo + razao
    cont = cont + 1
print('Fim!')