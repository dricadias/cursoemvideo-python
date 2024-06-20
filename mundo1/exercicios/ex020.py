import random
n1 = str(input('Digite seu nome: '))
n2 = str(input('Digite seu nome: '))
n3 = str(input('Digite seu nome: '))
n4 = str(input('Digite seu nome: '))
nomes = [n1, n2, n3, n4]
r = random.shuffle(nomes)
print("Ordem de apresentação: ")
for i, nomes in enumerate(nomes, start=1):   # essa parte fiz pesquisando pq nao tava conseguindo
    print(f'{i}. {nomes}')

# resolucao do gustavo

c1 = str(input('Digite seu nome: '))
c2 = str(input('Digite seu nome: '))
c3 = str(input('Digite seu nome: '))
c4 = str(input('Digite seu nome: '))
nms = [c1, c2, c3, c4]
random.shuffle(nms)
print("Ordem de apresentação: ")
print(nms)
