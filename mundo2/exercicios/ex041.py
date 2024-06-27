from datetime import date
ano = int(input('Digite o ano de nascimento: '))
at = date.today().year
idd = at - ano

if idd <= 9:
    print(f'Você tem {idd} anos e está na categoria \033[34mMIRIM\033[m')
elif idd <= 14:
    print(f'Você tem {idd} anos e está na categoria \033[34mINFANTIL\033[m')
elif idd <= 19:
    print(f'Você tem {idd} anos e está na categoria \033[34mJUNIOR\033[m')
elif idd <= 25:
    print(f'Você tem {idd} anos e está na categoria \033[34mSÊNIOR\033[m')
else:
    print(f'Você tem {idd} anos e está na categoria \033[34mMASTER\033[m')

# vi a resolucao agora e o que eu poderia ter mehorado é so o trabalho que deu colocando
# a idade em todos, eu poderia ter colocado apenas um print com a idade antes do primeiro if
# e as condicoes serem apenas a categoria, mas tudo bem!
