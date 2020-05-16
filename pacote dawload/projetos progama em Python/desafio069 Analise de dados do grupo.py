#desafio069 Análize de Dados do grupo
# Crie um progama que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o progama deverá
# perguntar se o usuario quer ou não continuar. No final mostre:
# A) Quantas pessoas tem mais de 18 anos
# B) Quantos homens foram cadastrados
# C) quantas mulheres tem menos de 20 anos
status = True
cont_idade = cont_mulheres = cont_homem = 0
while status:
    print('-=-'*20)
    print('Cadastre uma pessoa')
    print('-=-'*20)
    opcao = 'SN'
    while opcao == 'S':
        idade = int(input('Idade:'))
        sexo = str(input('Sexo: [M/F]').strip().upper()[0])
        opcao = str(input('Quer continuar? [S/N]').strip().upper()[0])
        if idade >= 18:
            cont_idade = cont_idade + 1
        elif sexo == 'F' and idade < 20:
            cont_mulheres = cont_mulheres + 1
        if sexo == 'M':
            cont_homem = cont_homem + 1
    print(f'{cont_idade} pessoas com mais de 18 anos')
    print(f'{cont_homem} homen(s) cadastrado(s)')
    print(f'{cont_mulheres} mulhere(s) tem menos de 20 anos')
    if opcao == 'N':
        status = False
        print('Finalizando sistema....')


