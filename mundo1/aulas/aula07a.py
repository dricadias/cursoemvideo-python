n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma é {s}, a multiplicação é {m}, a divisão é {d:.2f}, a divisão inteira é {di} e a exponenciação é {e}')


n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('\n A soma é {}, a multiplicação é {}, \n a divisão é {:.3f}, a divisão inteira é {} \n e a exponenciação é {}'.format(s, m, d, di, e))


n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, a multiplicação é {}, a divisão é {:.2f}'.format(s, m, d), end=', ')
print('divisão inteira {} e pontência {}'.format(di, e))
