#desafio069 Análize de Dados do grupo
# Crie um progama que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o progama deverá
# perguntar se o usuario quer ou não continuar. No final mostre:
# A) Quantas pessoas tem mais de 18 anos
# B) Quantos homens foram cadastrados
# C) quantas mulheres tem menos de 20 anos
status = True
cont_idade = cont_homem = cont_mulher = 0
while status:
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo:')).strip().upper()[0]
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar [S/N]:')).strip().upper()[0]
        if idade > 18:
            cont_idade = cont_idade + 1
        if sexo == 'M':
            cont_homem = cont_homem + 1
        if sexo == 'F':
            if idade < 20:
                cont_mulher = cont_mulher + 1
        if opcao == 'N':
            status = False
print(f'{cont_idade} pessoas são maiores de 18 anos')
print(f'{cont_homem} homen(s) cadastrados.')
print(f'{cont_mulher} mulher(es) cadastradas com menos de 20 anos')
print('Finalizando o processo!')


