import random
from time import sleep

j1 = str(input('Digite pedra, papel ou tesoura: ')).title().strip()
pc = random.choice(['Pedra', 'Papel', 'Tesoura'])
print('\033[32mPROCESSANDO...\033[m')
sleep(2)
if j1 == pc:
    print(f'\033[34mEMPATAMOS\033[m! EU PENSEI EM "\033[97m{pc.upper()}\033[m" TAMBÉM, '
          f'mas na próxima irei te vencer HAHAHA.')
elif j1 != pc:
    if j1 == 'Pedra' and pc == 'Tesoura':
        print(f'\033[31mNÃOOOOOO\033[m!!! EU PENSEI EM "\033[97m{pc.upper()}\033[m", \033[32mVOCÊ ME DERROTOU\033[m')
        print('\033[1;97mME DÊ OUTRA CHANCE!!!\033[m')
    elif j1 == 'Papel' and pc == 'Tesoura':
        print(f'\033[31mVOCÊ PERDEU\033[m!!! EU PENSEI EM "\033[97m{pc.upper()}\033[m" HAHAHAHA')
        print('\033[1;97mVOU TE DAR OUTRA CHANCE\033[m')
    elif j1 == 'Pedra' and pc == 'Papel':
        print(f'\033[31mVOCÊ PERDEU\033[m!!! EU PENSEI EM "\033[97m{pc.upper()}\033[m" HAHAHAHA')
        print('\033[1;97mVOU TE DAR OUTRA CHANCE\033[m')
    elif j1 == 'Papel' and pc == 'Pedra':
        print(f'\033[31mNÃOOOOOO\033[m!!! EU PENSEI EM "\033[97m{pc.upper()}\033[m", \033[32mVOCÊ ME DERROTOU\033[m')
        print('\033[1;97mME DÊ OUTRA CHANCE!!!\033[m')
    elif j1 == 'Tesoura' and pc == 'Papel':
        print(f'\033[31mNÃOOOOOO\033[m!!! EU PENSEI EM "\033[97m{pc.upper()}\033[m", \033[32mVOCÊ ME DERROTOU\033[m')
        print('\033[1;97mME DÊ OUTRA CHANCE!!!\033[m')
    else:  # j1 == 'Tesoura' and pc == 'Pedra':
        print(f'\033[31mVOCÊ PERDEU\033[m!!! EU PENSEI EM "\033[97m{pc.upper()}\033[m" HAHAHAHA')
        print('\033[1;97mVOU TE DAR OUTRA CHANCE\033[m')
else:
    print('JOGADA INVÁLIDA. TENTE NOVAMENTE')  # nao funfa
