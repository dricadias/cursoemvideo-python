s = float(input('Qual seu salário? R$'))
s1 = s + (s * 10 / 100)
s2 = s + (s * 15 / 100)

if s > 1250:
    print(f'Parabéns você ganhou um aumento de 10% ficando com {s1:.2f} de salário!')
else:
    print(f'Parabéns você ganhou um aumento de 15% ficando com {s2:.2f} de salário!')

# metodo do gustavo (prof)

s = float(input('Qual é o salário do funcionário? R$'))
if s > 1250.00:
    sn = s + (s * 10 / 100)
else:
    sn = s + (s * 15 / 100)
print(f'Quem ganhava R${s:.2f} passa a ganhar {sn:.2f}!')
