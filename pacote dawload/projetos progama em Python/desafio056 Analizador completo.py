#Desafio056 Analisador completo
# Desenvolva um progama que leia o nome, idade e sexo de 4 pessoas.No final do progama, mostre:
# 1 A media de idade do grupo.
# 2 Qual é o nome do homem mais velho.
# 3 Quantas mulheres tem menos de 20 anos.

print('-=-'*10)
print('Analizador completo')
print('-=-'*10)
soma_idade = 0
media_idade = 0
maioridadehomem = 0
nomevelho = ''
total_mulheres20 = 0
for c in range(1, 5):
    print('------ {}º Pessoa ------'.format(c))
    nome = str(input('Nome:').strip().upper())
    idade = int(input('Idade:'))
    sexo = str(input('Opçaõ sexo: [M] Masculino [F] Feminino:').strip().upper())
    soma_idade = soma_idade + idade
    if c == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        total_mulheres20 = total_mulheres20 + 1
media_idade = soma_idade / 4
print('A media de idade do grupo é de {} anos'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Aõ todo são {} mulheres com menos de 20 anos'.format(total_mulheres20))




