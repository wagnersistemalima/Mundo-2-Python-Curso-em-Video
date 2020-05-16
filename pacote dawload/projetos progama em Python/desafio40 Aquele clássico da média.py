#desafio40. Crie um progama que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
# final, de acordo com a média atingida:
# Media abaixo de 5.0: reprovado
# Média entre 5.0 e 6.9: Recuperação
# Média 7.0 ou superior: Aprovado
import math
nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
media = ((nota1 + nota2) / 2)
if media >= 7.0:
    print('Quem tirou {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
    print('O aluno está APROVADO!')
elif media >= 5.0 and media < 7.0:
    print('Quem tirou {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
    print('O aluno está em RECUPERAÇÂO.')
elif media < 5.0:
    print('Quem tirou {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
    print('O aluno está Reprovado!')


