#desafio 42. Refaça o desafio 35. dos triãngulos, acrecentando o recurso de mostrar que tipo de triângiulo,
# será formado: Equilátero: todos os lados iguais.
# Isóceles: dois lados iguais.
# Escaleno: Todos os lados diferentes.
a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))
if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
    print('Os segmentos acima podem formar um triangulo')
    if a == b and b == c:
        print('Equilatero')
    elif a != b and b != c and a != c:
        print('Escaleno')
    else:
        print('Isóceles')
else:
    print('Os segmentos acima não podem formar triângulo')


