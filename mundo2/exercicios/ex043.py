peso = float(input('Digite seu peso em kg: '))
alt = float(input('Digite sua altura em metros: '))
imc = peso / (alt * alt)

if imc < 18.5:
    print(f'Seu IMC é de {imc:.1f} e você está \033[1;31mABAIXO DO PESO\033[m.')
elif imc == 18.5 or imc < 25:  # 18.5 <= imc < 25: (modelo do gustavo)
    print(f'Seu IMC é {imc:.1f} e você está no \033[1;32mPESO IDEAL\033[m')
elif imc == 25 or imc < 30:  # 25 <= imc < 30 (modelo do gustavo)
    print(f'Seu IMC é {imc:.1f} e você está com \033[1;31mSOBREPESO\033[m')
elif imc == 30 or imc < 40:  # 30 <= imc < 40 (modelo do gustavo)
    print(f'Seu IMC é {imc:.1f} e você está com \033[1;31mOBESIDADE\033[m')
else:  # imc >= 40:
    print(f'Seu IMC é {imc:.1f} e você está com \033[1;31mOBESIDADE MÓRBIDA\033[m')

# vi a resolucao agora e o que eu poderia ter mehorado é so o trabalho que deu colocando
# o imc em todos, eu poderia ter colocado apenas um print com ele antes do primeiro if
# e as condicoes serem apenas a categoria, mas tudo bem!
