# Faça um programa que mostre a tabuada de varios numeros um de cada vez para cada valor
# digitado pelo usuario o programa sera interrompido quando o numero solicitado for negativo.


# Programa que mostra a tabuada de vários números
# O programa só para quando o usuário digitar um número negativo

while True:  # Loop infinito (vai repetir até ser interrompido com break)

    # Solicita ao usuário um número inteiro
    num = int(input('Quer ver a tabuada de qual valor? '))

    # Verifica se o número é negativo
    if num < 0:
        break  # Encerra o programa se for negativo

    print('-' * 20)  # Linha decorativa

    # Loop que vai de 1 até 10 (tabuada padrão)
    for c in range(1, 11):
        # Calcula o resultado da multiplicação
        resultado = c * num

        # Mostra o resultado formatado
        # {c:2} serve para alinhar o número em 2 espaços
        print(f'{num} x {c:2} = {resultado}')

    print('-' * 20)  # Linha decorativa após a tabuada

# Mensagem final quando o programa for encerrado
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')