nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas é:', nome.upper())
print('Seu nome em minúsculas é:', nome.lower())

print('A quantidade de caractere sem contar espaço é de:', len(nome.replace(' ', "")))  # posso usar essas duas formulas
print('A quantidade de caractere sem contar espaço é de:', len(''.join(nome.split())))  # pra essa questao
print('A quantidade de caractere sem contar espaço é de:', len(nome) - nome.count(' '))  # modelo do gustavo

div = nome.split()
print(f'Seu primeiro nome tem {len(div[0][0:])} letras')
print(f'Seu primeiro nome é {div[0]} e ele tem {len(div[0])} letras')  # modelo do gustavo
