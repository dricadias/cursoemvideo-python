import random
c1 = str(input('Digite seu nome: '))
c2 = str(input('Digite seu nome: '))
c3 = str(input('Digite seu nome: '))
c4 = str(input('Digite seu nome: '))
nomes = [c1, c2, c3, c4]
r = random.choice(nomes)
print(f'o aluno escolhido foi: {r}')

# ou com nomes prontos

nms = ["gustavo", "gus", 'gugu', "gu"]
res = random.choice(nms)
print(f'o aluno escolhido foi: {res}')
