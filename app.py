from module_from_import.modelos.restaurantes import Restaurante

restaurante_praca = Restaurante('Restaurante praça', 'lanchonete', False)
restaurante_praca.receber_avaliacao("Gui", 4)
restaurante_praca.receber_avaliacao("Leo", 5)
restaurante_praca.receber_avaliacao("Gabi", 2)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()