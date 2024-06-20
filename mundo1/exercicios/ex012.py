p = float(input('Qual valor do produto? R$'))
d = 5 * p / 100
dt = p - d
print(f'O valor do produto é R${p}, mas está na promoção com desconto de 5% por R${dt:.2f}')

# duas formas

p = float(input('Qual valor do produto? R$'))
d = p * 0.05
dt = p - d
print(f'O valor do produto é R${p}, mas está na promoção com desconto de 5% por R${dt:.2f}')

# outro modelo do gustavo com menos uma variavel (e mais fácil pelo amor

p = float(input('Qual valor do produto? R$'))
d = p - (p * 5 / 100)
print(f'O valor do produto é R${p}, mas está na promoção com desconto de 5% por R${d:.2f}')
