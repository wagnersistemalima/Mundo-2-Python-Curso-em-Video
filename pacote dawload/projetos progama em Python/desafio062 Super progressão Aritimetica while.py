#desafio062 Super progressão Aritimetica while
# Melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais alguns termos. O progama
# encerra guando ele disser que quer mostrar 0 termos.
print('Gerador de PA')
print('-=-'*10)
termo = int(input('Primeiro termo:'))     # inicio
razao = int(input('Razão:'))     # passo
cont = 1
total = 0
opcao_mais = 10
while opcao_mais != 0:
    total = total + opcao_mais
    while cont <= total:
        print('{}'.format(termo), end=' , ')
        termo = termo + razao
        cont = cont + 1
    print('Pausa!')
    opcao_mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
