m = float(input('Digite um valor em metro: '))
dm = m * 10
c = m * 100
mm = m * 1000
km = m / 1000
hm = m / 100
dam = m / 10
#print(f'O valor em metro é igual a {m}m, que corresponde a {c:.0f}cm e {mm:.0f}mm')
print(f'A medida de {m}m corresponde a \n{km}km \n{hm}hm \n{dam}dam \n{dm:.0f}dm \n{c:.0f}cm \n{mm:.0f}mm')
