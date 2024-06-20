tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')

#  posso ainda fazer essa condicao simplificada mas é mais 'baguncada'

tempo = int(input('Quantos anos seu carro tem? '))
print('Carro novo' if tempo <=3 else 'Carro velho')
print('--FIM--')
