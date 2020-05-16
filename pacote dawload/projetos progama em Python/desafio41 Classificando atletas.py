#desafio 41. A confederação Nacional de natação precisa de um progama que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com sua idade:
# Até 9 anos: Mirim. / Até 14 anos Infantil. / Até 19 anos Junior. / Até 25 anos Senior. / Acima: Master
from datetime import date
nascimento = int(input('Ano de Nascimento: '))
ano_atual = date.today().year  # função de importar o ano atual
idade = ano_atual - nascimento
if idade <= 9:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: Mirim')
elif idade > 9 and idade <= 14:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação Infatil')
elif idade > 14 and idade <= 19:
    print('O atleta tem {} anos.'.format(idade))
    print('classificação Junior')
elif idade > 19 and idade <= 25:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação Senior')
elif idade > 25:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação Master')
