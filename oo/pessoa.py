class Pessoa:
    def __init__(self, nome=None):
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {self.nome}'

if __name__ == '__main__':
    p = Pessoa('Marcelo')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())