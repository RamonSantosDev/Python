from classes.Conta import Conta
from classes.Cliente import Cliente
from classes.ContaEspecial import ContaEspecial

#TESTANDO O CODIGO
cliente1 = Cliente('123', 'joao', 'Rua y')
cliente2 = Cliente('231', 'maria', 'rua x' )
cliente3 = Cliente('444', 'Ramon', 'Rua J')
cliente4 = Cliente('555', 'Débora', 'Rua J')

conta1 = Conta([cliente1, cliente2], 111, 0)
conta2 = Conta([cliente3, cliente4], 222, 1621)
conta3 = ContaEspecial(cliente3, 3, 2000, 1000)



conta3.sacar(2800)
conta3.gerar_saldo()



