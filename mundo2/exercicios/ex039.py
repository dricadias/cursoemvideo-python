from datetime import date
sexo = int(input('Qual seu sexo? \n[1] para FEMININO\n[2] para MASCULINO\nDigite: '))
if sexo == 1:
    print('Seu alistamento militar \033[30mNÃO\033[m é obrigatório!')
elif sexo == 2:
    ano = int(input('Digite o ano de nascimento: '))
    aa = date.today().year
    dt = aa - ano
    if dt < 17:
        saldo = 18 - dt
        print(f'Você tem {dt} anos, ainda \033[1;31mnão\033[m precisa se alistar, só daqui há {saldo} anos.')
        af = aa + saldo
        print(f'Seu alistamento será em {af}.')
    elif dt == 17:
        saldo = 18 - dt
        print(f'Você tem {dt} anos, ainda \033[1;31mnão\033[m precisa se alistar, só daqui há {saldo} ano.')
        af = aa + saldo
        print(f'Seu alistamento será em {af}.')
    elif dt == 18:
        print(f'Você tem {dt} anos, \033[1;32mestá na hora\033[m de se alistar!')
    elif dt == 19:
        saldo = dt - 18
        print(f'Você tem {dt} anos, \033[1;31mjá passou\033[m {saldo} ano do tempo de alistamento.')
        af = aa - saldo
        print(f'Seu alistamento foi em {af}.')
    else:
        saldo = dt - 18
        print(f'Você tem {dt} anos, \033[1;31mjá passou\033[m {saldo} anos do tempo de alistamento.')
        af = aa - saldo
        print(f'Seu alistamento foi em {af}.')
else:
    print('Opção inválida. Tente novamente.')

# eu quis deixar o codigo mais completo e sem o erro de digitacao de '1 anos' ou '2 ano'
# fiz do jeito que sei ate agora
