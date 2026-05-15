# Criar um programa que leia varios numeros inteiros pelo teclado. o programa so vai parar quando
# o usuario digitar o valor 999 no final mostra quantos numeros foi digitado e a soma entre eles.


num = cont = s = 0
while True:
    num = int(input('Digite um número: (999 para parar): '))
    if num == 999:
        break
    cont += 1
    s += num
print(f'A soma dos {cont} valores foi {s}!')