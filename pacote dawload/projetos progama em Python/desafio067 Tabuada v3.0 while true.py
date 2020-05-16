# desafio067 Tabuada v3.0
# Faça um progama que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo
# Usuario. o progama será interrompido quando o numero solicitado for negativo.
while True:
    numero = int(input('Digite um numero para calcular sua tabuada:'))
    print('-'*30)
    if numero < 0:
        break
    for c in range(1, 11):
        print(f'{c} x {numero} = {c * numero}')
    print('-'*30)
print('PROGAMA ENCERRADO COM SUCESSO! Volte sempre!')


