print("olá, mundo!")

#so um teste

nome=("gustavo")
print(nome, "é a pessoa mais idiota do mundo")

def menorelm (lista):
   menor = lista [0]
   for elem in lista:
       if elem < menor:
          menor = elem
   return menor
l = [12,-12,6,2,0]
print(menorelm(l))


MI = []
for i in range (5):
   linha = []
   for j in range (5):
      if i == j:
          linha.append(1)
      else:
           linha.append(0)
   MI.append(linha)
for linha in MI:
   print(linha)


def mat_maior_10 (matriz):
    cont = 0
    for linha in matriz:
        for elem in linha:
            if elem < 10:
                cont +=1
    return cont
M = [11,2], [30,4],[52,6]
print(mat_maior_10(M))


def mat_transposta (matriz):
    T = []
    for i in range (len(matriz[0])):
        linha = []
        for j in range (len(matriz)):
            linha.append(matriz[j][i])
        T.append(linha)
        return T
M = [[1,2],[3,4],[5,6]]

for linha in mat_transposta(M):
    print(linha)
