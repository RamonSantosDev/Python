import datetime
from classes.Extrato import Extrato

class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(['DEPOSITO', valor, datetime.datetime.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(['SAQUE', valor, datetime.datetime.today()])
            return True

    def tranferencia_valor(self, conta_destino, valor):
        if self.saldo < valor:
            return 'Não existe saldo suficiente'
        else:
            conta_destino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(['TRANSFERENCIA', valor, datetime.datetime.today()])
        return 'transferencia realizada!'

    def gerar_saldo(self):
        print(f'Número: {self.numero}\nsaldo: {self.saldo}')
