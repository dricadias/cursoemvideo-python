nome = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra A aparece {nome.count("A")} vezes na frase.')
print(f'A primeira letra A apareceu na posição {nome.find("A")+1}')
print(f'A última letra A apareceu na posição {nome.rfind("A")+1}')
