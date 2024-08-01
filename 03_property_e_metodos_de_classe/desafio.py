class ContaBancaria:
    clientes = []
    def __init__(self, titular='', saldo=0, ativo=False):
        self._titular = titular
        self._saldo = saldo
        self._ativo = ativo
        ContaBancaria.clientes.append(self)

    def __str__(self):
        return f'{self._titular}, você tem R$ {self._saldo},00 na sua conta'

    @classmethod
    def listar_clientes(cls):
        for cliente in cls.clientes:
            print(f'{cliente._titular} | {cliente._saldo} | {cliente.ativo}')

    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'
    
    def ativar_conta(self):
        self._ativo = not self._ativo


cliente_1 = ContaBancaria('Thomas', 250)
cliente_1.ativar_conta()
cliente_2 = ContaBancaria('Luciana', 15)
ContaBancaria.listar_clientes()
