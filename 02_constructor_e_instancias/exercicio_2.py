#exercicio 2:

class Restaurante:
    restaurantes = []
    def __init__(self, nome='', categoria ='', ativo=False, descricao='', nota=0.0):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.descricao = descricao
        self.nota = nota
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo} | {self.descricao} | {self.nota}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.descricao} | {restaurante.nota}')
#exercicio 3:

restaurante_1 = Restaurante('Casa do pão', 'Padaria', False, 'Padaria muito boa', 4.5)

Restaurante.listar_restaurantes()
