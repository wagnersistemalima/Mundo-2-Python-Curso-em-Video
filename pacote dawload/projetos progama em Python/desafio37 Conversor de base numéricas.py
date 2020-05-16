# desafio37. escreva um progama que leia um número inteiro qualquer e peça para o usuário escolher qual
# será a base de conversão: 1 para binario. / 2 para octal/ 3 hexadecimal.
entrada = int(input('Digite um numero inteiro:'))
print('''Escolha uma das bases para converção:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é iqual a {}'.format(entrada, bin(entrada)[2:]))
elif opcao == 2:
    print('{} convertido para BINÀRIO é iqual a {}'.format(entrada, oct(entrada)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é iqual a {}'.format(entrada, hex(entrada)[2:]))
else:
    print('Opção invalida! Tente novamente!')


