pessoas = {'nome': 'Ramon', 'idade': 30}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas['idade']
pessoas['nome'] = 'Debora'
pessoas['idade'] = 25
pessoas['peso'] = 58
for k, v in pessoas.items():
    print(f'{k} = {v}')
    