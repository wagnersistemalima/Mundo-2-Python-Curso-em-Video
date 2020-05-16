#desafio43. Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule se IMC e mostre seu status,
# de acordo com a tabela abaixo:
# Abaixo de 18.5; Abaixo do peso    /   25 até 30: Sobrepeso
# Entre 18.5 e 25: peso ideal.      /   30 até 40; Obesidade
# Acima de 40: Obesidade Mórbida.
peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('Você está abaixo do peso normal.')
elif imc >= 18.5 and imc < 25:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print(' Você está no Peso ideal')
elif imc >= 25 and imc < 30:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('Você está com Sobrepeso')
elif imc >= 30 and imc < 40:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('Você está com Obesidade')
elif imc >= 40:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('Você está com Obesidade Mórbida')




