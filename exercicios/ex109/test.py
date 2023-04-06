# FORMATANDO MOEDAS EM PYTHON

from ex109 import moeda

def aumentar(preço = 0, taxa = 0, formato = False):
    '''
    ~~~
    :param preço:
    :param taxa:
    :param formato:
    :return:
    ~~~
    '''
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)