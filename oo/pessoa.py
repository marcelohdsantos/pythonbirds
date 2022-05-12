class Pessoa:
    olhos = 2   # atributo de classe
    def __init__(self, *filhos, nome=None):
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self.nome}'

if __name__ == '__main__':
  marcelo = Pessoa(nome='Marcelo')
  andre = Pessoa(nome='André')

  maria = Pessoa({andre, marcelo}, nome='Maria')
  maria = Pessoa(andre, nome='Maria')

  for filho in maria.filhos:
      print(filho.nome)

marcelo.sobrenome = 'Dos Santos'
del maria.filhos
del marcelo.sobrenome
marcelo.olhos = 1
print(Pessoa.olhos)
print(andre.__dict__)
print(marcelo.olhos)
print(maria.__dict__)
print(marcelo.__dict__)


