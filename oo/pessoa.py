class Pessoa:
    def __init__(self, *filhos, nome=None):
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self.nome}'

if __name__ == '__main__':
    marcelo = Pessoa(nome='Marcelo')
    maria = Pessoa(marcelo, nome='Maria')
    for filho in maria.filhos:
        print(filho.nome)
