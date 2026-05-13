from classes.Conta import Conta
from classes.Cliente import Cliente


#TESTANDO O CODIGO
cliente1 = Cliente('123', 'joao', 'Rua y')
cliente2 = Cliente('231', 'maria', 'rua x' )
cliente3 = Cliente('444', 'Ramon', 'Rua J')
cliente4 = Cliente('555', 'Débora', 'Rua J')

conta1 = Conta([cliente1, cliente2], 111, 0)
conta2 = Conta([cliente3, cliente4], 222, 1621)

conta1.depositar(1000)
conta1.tranferencia_valor(conta2, 100)
conta1.extrato.gera_extrato(conta1.numero)
conta2.extrato.gera_extrato(conta2.numero)



