#Desafio053 Detector de Palidromo.
#Faça um progama que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
# Ex: APOS A SOPA / A SACADA DA CASA / A TORRE DA DERROTA / O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA

frase = str(input().strip().upper())
print('Você digitou a frase: {}!'.format(frase))
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
#for letra in range(len(junto) - 1, -1, -1):
#    inverso = inverso + junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palidromo')
else:
    print('A frase digitada não é um palidromo.')
