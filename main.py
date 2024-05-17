class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.transacoes = []

    def deposito(self, valor):
        self.saldo += valor
        self.transacoes.append(('Depósito', valor))

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.transacoes.append(('Saque', valor))
        else:
            print("Saldo insuficiente para realizar o saque.")

    def extrato(self):
        print("Extrato da Conta:")
        print(f"Saldo atual: R${self.saldo}")
        print("Transações:")
        for tipo, valor in self.transacoes:
            print(f"{tipo}: R${valor}")


conta = ContaBancaria(100)
conta.deposito(50)
conta.saque(30)
conta.saque(200)
conta.extrato()
