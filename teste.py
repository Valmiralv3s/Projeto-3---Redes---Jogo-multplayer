class animal:
    def __init__(self, nome):
        self.nome = nome

    def dizerNome(self):
        print("Meu nome é " + self.nome)


class Gato(animal):
    def __init__(self, nome):
        super().__init__(nome)


mingau = Gato('mingau')
mingau.dizerNome()
