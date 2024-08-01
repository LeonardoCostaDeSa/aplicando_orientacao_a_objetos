#exercicio 2:

class Restaurante:
    restaurantes = []
    def __init__(self, nome='', categoria ='', ativo=False):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = ativo
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status".ljust(25)}\n')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'
    
    def alternar_estado(self):
        self._ativo = not self._ativo


restaurante_casa_do_pao = Restaurante('casa do pão', 'Padaria', False)
restaurante_2 = Restaurante('comida boa', 'Marmita', False)
restaurante_casa_do_pao.alternar_estado()
Restaurante.listar_restaurantes()
