# CALCULANDO DESCONTOS

n1 = float(input('Preço: '))
r = n1
r1 = n1 * 5 / 100
r2 = n1 - r1
print('O preço original é de {}, e com o desconto é de {:.2f}.'.format(n1, r2))