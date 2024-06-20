s = float(input('Qual seu salário? R$'))
a = s * 0.15
at = s + a
print(f'O salário de R${s} com o aumento de 15% ficou por R${at:.2f}')


s = float(input('Qual seu salário? R$'))
a = s + (s * 15 / 100)
print(f'O salário de R${s} com o aumento de 15% ficou por R${a:.2f}')
