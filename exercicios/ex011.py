# PINTANDO PAREDE

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {} x {} e area é de {:.1f}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {:.1f}l de tinta.'.format(tinta))