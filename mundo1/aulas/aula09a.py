frase = 'Curso em Vídeo Python'
print(frase[0:15:2])

print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python', 'Android'))
print('Curso' in frase)
print(frase.find('Vídeo'))
print(frase.lower().find('vídeo'))
print(frase.split())

dividido = frase.split()
print(dividido[2][3])  # pega o dividido 2 que é Video e me mostra a letra 3
