#desafio36. Escreva um progama para aprovar o empréstimo bancario para a compra de uma casa. O progama vai perguntar,
# o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
#calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o empréstimo será negado.
v_casa = float(input('O valor da casa R$'))
salario = float(input('Salario do comprador R$'))
anos = int(input('Em quantos anos vai pagar?'))
parcela = v_casa / (anos * 12)
limite = salario * 30 / 100
if parcela > limite:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(v_casa, anos, parcela))
    print('Empréstimo NEGADO!')
elif parcela <= limite:
    liberado = parcela
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(v_casa, anos, liberado))
    print('Empréstimo pode ser CONCEDIDO!')






