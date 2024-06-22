casa = float(input('Digite o valor da casa que você quer comprar? R$'))
sal = float(input('Digite seu salário atual: R$'))
anos = int(input('Em quantos anos você pretende pagar? '))

pres = casa / (anos * 12)
por = sal * 30 / 100

print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos, a prestação será de R${pres:.2f}')

if pres > por:
    print('\033[31mSeu empréstimo foi negado!\033[m')
else:
    print('\033[32mParabéns! Você conseguiu o empréstimo.\033[m')

# print(por, pres)
