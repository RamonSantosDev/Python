'''teste = list()
teste.append('Ramon')
teste.append(30)
galera = list()
galera.append(teste[:])
teste[0] = 'Debora'
teste[1] = 25
galera.append(teste[:])
teste[0] = 'Luzia'
teste[1] = 60
galera.append(teste[:])
print(galera)'''

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):# Laço que vai repetir 3 vezes
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # cria uma copia e armazena na variavel composta galera
    dado.clear()
for p in galera: # para cada pessoa na lista galeria fazer
     if p[1] >= 18:
         print(f'{p[0]} é maior de idade')
         totmai += 1
     else:
         print(f'{p[0]} é menor de idade')
         totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade')

