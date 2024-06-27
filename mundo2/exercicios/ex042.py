l1 = float(input('Digite um comprimento: '))
l2 = float(input('Digite outro comprimento: '))
l3 = float(input('Digite outro comprimento: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Os comprimentos acima \033[1;32mPODEM\033[m formar um triângulo!.')
    if l1 == l2 == l3:  # tinha feito assim antes "l1 == l2 and l2 == l3", mas pode fazer dessa outra forma tbm
        print('O triangulo formado é \033[1;33mEQUILÁTERO\033[m.')
    elif l1 == l2 or l3 == l1 or l2 == l3:
        print('O triângulo formado é \033[1;33mISÓSCELES\033[m.')
    else:  # r1 != r2 != r3 != r1:
        print('O triângulo formado é \033[1;33mESCALENO\033[m.')
else:
    print('Os comprimentos acima \033[1;31mNÃO PODEM\033[m formar um triângulo.')
