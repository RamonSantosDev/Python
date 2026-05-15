def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um numero inteiro valido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mUsuario preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaReal(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um numero real valido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mUsuario preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n



n1 = leiaInt('Digite um numero inteiro: ')
n2 = leiaReal('Digite um numero Real: ')
print(f'O numero inteiro digitado foi {n1} e o Real foi {n2}' )






