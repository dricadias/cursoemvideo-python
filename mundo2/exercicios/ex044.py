v = float(input('Qual valor da sua compra? R$'))
m = int(input('1 - Á vista em Dinheiro/Cheque'
              '\n2 - Á vista no cartão'
              '\n3 - Até 2x no cartão'
              '\n4 - 3x ou mais no cartão'
              '\nDigite o método de pagamento considerando os números acima: '))
din = v - (v * 10 / 100)
car = v - (v * 5 / 100)
# car 2 é = v
car3 = v + (v * 20 / 100)

if m == 1:
    print(f'Você recebeu um \033[1;32mdesconto de 10%\033[m, ficando o valor total \033[1;32mR${din:.2f}\033[m!')
elif m == 2:
    print(f'Você recebeu um \033[1;32mdesconto de 10%\033[m, ficando o valor total \033[1;32mR${car:.2f}\033[m!')
elif m == 3:
    parc = v / 2
    print(f'Sua compra sera parcelada em 2x de R${parc:.2f}')
    print(f'O valor total é \033[1;97mR${v:.2f}\033[m!')
elif m == 4:
    totparc = int(input('Quantas parcelas? '))
    parc = car3 / totparc
    print(f'Sua compra será parcelada em {totparc}x de \033[1;31mR${parc:.2f}\033[m!')
    print(f'Você vai receber um \033[1;31mjuros de 20%\033[m, ficando o valor total \033[1;31mR${car3:.2f}\033[m!')
else:
    print('\033[31mOpção de pagamento inválida. Tente novamente.\033[m')

# vi a resolucao agora e o que eu poderia ter mehorado é so o trabalho que deu colocando
# o valor em todos, eu poderia ter colocado apenas um print com ele antes ou depois do primeiro if
# e as condicoes serem apenas a categoria de pagamento e o que ia mudar nele, mas tudo bem!
