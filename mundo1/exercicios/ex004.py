n = input('Digite algo:')
print('O tipo primitivo desse valor é', type(n))
print('É numérico?', n.isnumeric())
print('É alfanumérico?', n.isalnum())
print('É alfabético?', n.isalpha())
print('É sempre maiúsculo?', n.isupper())
print('É sempre minúsculo?', n.islower())
print('Está capitalizado?', n.istitle())
print('Só tem espaços?', n.isspace())

#print('NÃO FIZ A SEGUNDA PARTE PQ ACHEI A PRIMEIRA MAIS DIDATICA E SIMPLES')
#print('MAS ESTOU DEIXANDO APENAS PARA OBSERVAÇÃO CASO PRECISE EM ALGUM MOMENTO!!!')

g = input('Digite algo:')
print(f'O tipo primitivo desse valor é {type(g)}')
print(f'É um número? {g.isnumeric()}')
print(f'É alfanumérico? {g.isalnum()}')
print(f'É alfabético? {g.isalpha()}')
print(f'Só tem espaços? {g.isspace()}')
print(f'É apenas minúsculo {g.islower()}')
print(f'É apenas maiúsculo? {g.isupper()}')
print(f'Está capitalizada? {g.istitle()}')































