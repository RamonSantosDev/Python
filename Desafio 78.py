# Cria uma lista vazia para armazenar os números digitados
lista = []

# Variáveis que irão guardar o maior e o menor valor
mai = 0
men = 0

# Laço que vai repetir 5 vezes
for c in range(0, 5):

    # Lê um número do usuário e adiciona na lista
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))

    # Se for o primeiro número digitado
    if c == 0:

        # O primeiro valor será considerado o maior e o menor inicialmente
        mai = men = lista[c]

    else:

        # Verifica se o valor atual é maior que o maior salvo
        if lista[c] > mai:

            # Atualiza o maior valor
            mai = lista[c]

        # Verifica se o valor atual é menor que o menor salvo
        if lista[c] < men:

            # Atualiza o menor valor
            men = lista[c]

# Mostra todos os valores digitados
print(f'Voce digitou os valores {lista}')

# Mostra o maior valor encontrado
print(f'O maior valor digitado foi {mai} nas Posiçoes ', end='')

# Percorre a lista mostrando as posições do maior valor
for i, v in enumerate(lista):

    # Se o valor da posição for igual ao maior valor
    if v == mai:

        # Mostra a posição
        print(f'{i}...', end="")

# Pula linha
print()

# Mostra o menor valor encontrado
print(f'O menor valor digitado foi {men} nas posições ', end='')

# Percorre a lista mostrando as posições do menor valor
for i, v in enumerate(lista):

    # Se o valor da posição for igual ao menor valor
    if v == men:

        # Mostra a posição
        print(f'{i}...', end='')

# Pula linha final
print()
