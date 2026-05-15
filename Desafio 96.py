def area(larg, comp):
    a = larg * comp
    print(f'A area do terreno {larg}x{comp} é de {a}m²')


print('Controle de terreno')
print('-'*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
