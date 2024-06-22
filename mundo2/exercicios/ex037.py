num = int(input('Digite um número inteiro: '))
print('Agora você terá que digitar \n1 para binário.\n2 para octal.\n3 para hexadecimal.')
c = int(input('Digite o número escolhido para conversão: '))

if c == 1:
    print(f'O número \033[33m{num}\033[m em binário é \033[32m{bin(num)[2:]}\033[m.')
elif c == 2:
    print(f'O número \033[33m{num}\033[m em octal é \033[32m{oct(num)[2:]}\033[m.')
elif c == 3:
    print(f'O número \033[33m{num}\033[m em hexadecimal é \033[32m{hex(num)[2:]}\033[m.')
else:
    print('Opção inválida. Tente novamente.')
