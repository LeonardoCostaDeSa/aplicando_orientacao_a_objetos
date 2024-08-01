class Musica:
    musicas = []
    def __init__(self, nome, artista, duracao):
        self.nome = str(nome)
        self.artista = str(artista)
        self.duracao = int(duracao)
        Musica.musicas.append(self)
    
    def __str___(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'
    
    def listar_musicas ():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')


musica_1 = Musica('Faroeste de coboclo', 'Legião Urbana', 850)
musica_2 = Musica('American Idiot', 'Green Day', 255)
Musica.listar_musicas()