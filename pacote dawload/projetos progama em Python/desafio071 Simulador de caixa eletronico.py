#Desafio Simulador de caixa eletronico
# Crie um progama que simule o funcionamento de um caixaeletrônico. No inicio, pergunte ao usuario
# qual será o valor a ser sacado (número inteiro) e o progama vai informar quantas cedulas de cada valor
# serão entregues. OBS: Considere o caixa possui cedulas de R$50,00 / R$20,00 / R$10,00 / R$1,00
print('{:-^40}'.format('Caixa Eletrônico'))
saque = int(input('Qual o valor a ser sacado?R$'))
montante = saque    # dinheiro do saque
maior_cedula = 50   # notas
cont_cedulas = 0    # quantidades de notas usadas
status = True
while status:
    if montante >= maior_cedula:      # Valor do saque da para tirar 50. tire 50 ate onde dé
        montante = montante - maior_cedula
        cont_cedulas = cont_cedulas + 1
    else:  #cedula de 50 passa 20 .se não de mais p tirar 50, resto do montante vai tirar 20 ate onde de
        if cont_cedulas > 0:    # desconcidera  0 notas
            print(f'{cont_cedulas} nota(s) de R${maior_cedula}')
        if maior_cedula == 50:
            maior_cedula = 20
        elif maior_cedula == 20:
            maior_cedula = 10
        elif maior_cedula == 10:
            maior_cedula = 1
        cont_cedulas = 0     # quantidade de celuas e zerada pois não ha mais o que dividir
        if montante == 0:         # Quando o montante tiver zerado. fim
            status = False




