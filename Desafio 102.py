from math import factorial

def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O numero a ser calculado.
    :param show: (opcional) Mostrar ou nao a conta.
    :return: o valor do Fatorial de um número n.
    """
    if show:
        f = 1
        for c in range(n, 0, -1):
            f *= c
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        return f
    else:
        return factorial(n)


print(fatorial(5, show=True))
