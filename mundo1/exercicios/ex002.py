nome = input('Digite seu nome:')
print('É um prazer te conhecer,', nome + '!')

nome = input('Qual é o seu nome? ')
print('É um grande prazer te conhecer, {}.'.format(nome))

nome = input('Qual seu nome? ')
print(f'É um prazer te conhecer, {nome}!')

#separando

#nome=input("Qual seu nome? ")
#print("Seja bem vindo,", nome)


#idade=input("Quantos anos você tem? ")
#objetivo=input("Qual seu objetivo? ")

nome = input('Qual é o seu nome? ')
print('É um grande prazer te conhecer, {:>12}.'.format(nome))