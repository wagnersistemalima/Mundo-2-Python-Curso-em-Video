#desafio057 Validação de dados while
#Faça um progama que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# caso esteja errado, peça a digitação novamente até ter um valor correto.
print('Digite [M] Masculino ou [F] Feminino')
opcao = str(input('Digite seu sexo: [M/F]:').strip().upper()[0])
while opcao != 'M' and opcao != 'F':
    opcao = str(input('Dados invalidos, por favor digite seu sexo: [M/F]:').strip().upper()[0])
print('Sexo {} registrado com sucesso!'.format(opcao))






