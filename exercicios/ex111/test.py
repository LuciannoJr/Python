# TRANSFORMANDO MODULOS EM PACOTES

from ex111.utilidades import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 20, 12)