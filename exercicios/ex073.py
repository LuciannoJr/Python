# TUPLAS COM TIMES DE FUTEBOL

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
        'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
        'Atlético', 'Botafogo', 'Athletico-PR', 'Bahia',
        'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
        'Atlético-GO')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros times são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 útimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posição')