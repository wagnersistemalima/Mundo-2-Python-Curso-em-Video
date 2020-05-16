#desafio39.faça um progama que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele
# ainda vai se alistar ao serviço militar, se é a hora certa de se alistar ou seja passou do tempo do alistamento.
#Seu progama tamêm deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
print('--=--'*12)
print('PROGAMA DE ALISTAMENTO BRASILEIRO!')
print('--=--'*12)
entrada = int(input('Digite o ano de seu nascimento:'))
print('''Sexo Masculino [1]
Sexo Feminino [2]''')
sexo = int(input("Sua opção: [1] ou [2] :"))
ano_atual = date.today().year # função de importar o ano atual.
idade = ano_atual - entrada
if sexo == 2:
    print('O alistamento é obrigatorio só para o SEXO MASCULINO!')
if idade > 18 and sexo == 1:
    alistamento = entrada + 18
    print('Quem nasceu em {} tem {} anos em {}.'.format(entrada, idade, ano_atual))
    print('Seu alistamento foi em {}.'.format(alistamento))
elif idade == 18 and sexo == 1:
    print('Quem nasceu em {} tem {} anos em {}.'.format(entrada, idade, ano_atual))
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18 and sexo == 1:
    alistamento = 18 - idade
    ano = ano_atual + alistamento
    print('Quem nasceu em {} tem {} anos em {}.'.format(entrada, idade, ano_atual))
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento.'.format(alistamento))
    print('Seu alistamento será em {}'.format(ano))
print('--=--'*12)
print('SISTEMA LIMA 2020.')


