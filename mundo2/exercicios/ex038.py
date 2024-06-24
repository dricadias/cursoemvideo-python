n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    print(f'O primeiro valor {n1} é \033[32mMAIOR\033[m que o segundo valor {n2}.')
elif n2 > n1:
    print(f'O segundo valor {n2} é \033[32mMAIOR\033[m que o primeiro valor {n1}.')
else:
    print(f'Os valores {n1} e {n2} são \033[32mIGUAIS\033[m.')
