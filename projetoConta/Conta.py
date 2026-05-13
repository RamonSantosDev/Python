# Classe Conta
# Serve como modelo para criar contas bancárias
class Conta:

    # Método construtor
    # É executado automaticamente quando um objeto é criado
    def __init__(self, numero, cpf, nomeTitular, saldo):

        # Atributos da conta
        self.numero = numero              # Número da conta
        self.cpf = cpf                    # CPF do titular
        self.nomeTitular = nomeTitular    # Nome do titular
        self.saldo = saldo                # Saldo da conta

    # Método para depositar dinheiro
    def depositar(self, valor):

        # Soma o valor depositado ao saldo atual
        self.saldo += valor

    # Método para sacar dinheiro
    def sacar(self, valor):

        # Verifica se existe saldo suficiente
        if self.saldo < valor:

            # Retorna False se não houver saldo
            return False

        else:
            # Diminui o valor do saldo
            self.saldo -= valor

            # Retorna True indicando sucesso
            return True

    # Método para mostrar os dados da conta
    def extrato(self):

        # Exibe as informações da conta
        print(f'número: {self.numero}')
        print(f'CPF: {self.cpf}')
        print(f'nome: {self.nomeTitular}')
        print(f'saldo: R${self.saldo:.2f}')

    # Método para transferir dinheiro para outra conta
    def transfereValor(self, contaDestino, valor):

        # Verifica se existe saldo suficiente
        if self.saldo < valor:

            # Retorna mensagem de erro
            return 'Não existe saldo suficiente'

        else:

            # Deposita o valor na conta destino
            contaDestino.depositar(valor)

            # Remove o valor da conta atual
            self.saldo -= valor

            # Retorna mensagem de sucesso
            return 'Transferencia realizada'


# ==========================================
# CRIANDO UMA CONTA
# ==========================================

# Criando o objeto c1
c1 = Conta(1, 5196144536, 'Ramon Nascimento', 9000)

# Depositando 500 reais na conta
c1.depositar(500)


# ==========================================
# REALIZANDO UM SAQUE
# ==========================================

# Valor que será sacado
valor_saque = 30

# Chamando o método sacar()
# O resultado será True ou False
resultado_saque = c1.sacar(valor_saque)

# Verifica se o saque foi realizado
if resultado_saque:

    # Executa se o retorno for True
    print(f'Saque de {valor_saque} realizado com sucesso!')

else:

    # Executa se o retorno for False
    print('Saldo insuficiente para realizar o saque')


# ==========================================
# MOSTRANDO EXTRATO
# ==========================================

# Exibe os dados da conta
c1.extrato()


# ==========================================
# CRIANDO OUTRAS CONTAS
# ==========================================

conta1 = Conta(123, 99999, 'Maria', 0)
conta2 = Conta(123, 99999, 'Maria', 500)


# ==========================================
# COMPARANDO OBJETOS
# ==========================================

# Aqui o Python compara os objetos na memória
# Mesmo com dados parecidos, são objetos diferentes
if conta1 == conta2:
    print('São iguais')

else:
    print('São diferentes')


# ==========================================
# TRANSFERÊNCIA ENTRE CONTAS
# ==========================================

# Transferindo 300 da conta2 para conta1
print(conta2.transfereValor(conta1, 300))


# ==========================================
# EXIBINDO EXTRATOS FINAIS
# ==========================================

# Mostra saldo atualizado da conta1
conta1.extrato()

# Mostra saldo atualizado da conta2
conta2.extrato()