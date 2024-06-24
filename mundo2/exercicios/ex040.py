n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

if m < 5.0:
    print(f'Sua média foi de {m:.1f} e você foi \033[31mREPROVADO!\033[m')
elif m == 5.0 or m < 7:  # posso fazer assim tbm "7 > m => 5:"
    print(f'Sua média foi de {m:.1f} e você está em \033[31mRECUPERAÇÃO!\033[m')
else:
    print(f'Sua média foi de {m:.1f} e você foi \033[32mAPROVADO!\033[m')
