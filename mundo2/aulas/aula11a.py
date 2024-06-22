print('\033[1;31;43mOlá, Mundo!\033[m')  # o codigo no final serve pra
print('\033[4;97;45mOlá, Mundo!\033[m')  # formatacao nao ficar uma linha gigante

a = 2
b = 5
print(f'Os valores são \033[1;36m{a}\033[m e \033[1;33m{b}\033[m')

nome = 'Gustavo'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'preto': '\033[30m'}

print(f'Prazer em te conhecer {cores["preto"]}{nome}{cores["limpa"]}!!!')
