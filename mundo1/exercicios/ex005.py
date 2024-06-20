ni = int(input('Digite um número: '))
ant = ni - 1
suc = ni + 1
print('O número inteiro é {}, o seu antecessor é {} e o seu sucessor é {}'.format(ni, ant, suc))

#ou pode ser com apenas uma variável

ni = int(input('Digite um número: '))
print('O número inteiro é {}, o seu antecessor é {} e o seu sucessor é {}'.format(ni, (ni-1), (ni+1)))
