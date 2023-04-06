# CLASSIFICANDO ATLETAS

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
if idade <= 9:
    print('O atleta possui {} anos. Classificação: Mirim.'.format(idade))
elif idade > 9 and idade <= 14:
    print('O atleta possui {} anos. Classificação: Infantil.'.format(idade))
elif idade > 14 and idade <=19:
    print('O atleta possui {} anos. Classificação: Junior.'.format(idade))
elif idade > 19 and idade <= 25:
    print('O atleta possui {} anos. Classificação: Senior.'.format(idade))
elif idade > 25:
    print('O atleta possui {} anos. Classificação: Master.'.format(idade))
