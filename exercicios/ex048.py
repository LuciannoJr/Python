# SOMA IMPARES MULTIPLOS DE TRES

soma = 0 #acumulador
cont = 0 #contador
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 #ou cont += 1
        soma = soma + c #ou soma += c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
