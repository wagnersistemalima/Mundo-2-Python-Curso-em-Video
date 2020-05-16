#Desafio Simulador de caixa eletronico
# Crie um progama que simule o funcionamento de um caixaeletrônico. No inicio, pergunte ao usuario
# qual será o valor a ser sacado (número inteiro) e o progama vai informar quantas cedulas de cada valor
# serão entregues. OBS: Considere o caixa possui cedulas de R$100,00 / R$50,00 / R$20,00 / R$10,00
# R$5,00 / R$2,00.
print('='*40)
print('{:^40}'.format('Caixa Eletrônico'))
print('='*40)
saque = int(input('Qual será o valor do saque?R$'))
montante = saque
maior_cedula = 100
maior_moeda = 0.50
cont_notas = cont_moedas = 0
status = True
while status:
    if montante >= maior_cedula:
        montante = montante - maior_cedula
        cont_notas = cont_notas + 1
        cont_moedas = cont_moedas + 1
    else:
        print(f'{cont_notas} nota(s) de R${maior_cedula}')
        if maior_cedula == 100:
            maior_cedula = 50
        elif maior_cedula == 50:
            maior_cedula = 20
        elif maior_cedula == 20:
            maior_cedula = 10
        elif maior_cedula == 10:
            maior_cedula = 5
        elif maior_cedula == 5:
            maior_cedula = 2
        elif maior_cedula == 2:
            maior_cedula = 1
        cont_notas = 0
        if montante == 0:
            status = False
