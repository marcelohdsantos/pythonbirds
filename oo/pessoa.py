class Pessoa:
    olhos = 2   # atributo de classe
    def __init__(self, *filhos, nome=None):
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def atributo_de_classe_e_nome(cls):
        return f'{cls}  {cls.olhos} -> olhos.'

if __name__ == '__main__':
  marcelo = Pessoa(nome='Marcelo')
  andre = Pessoa(nome='André')

  maria = Pessoa({andre, marcelo}, nome='Maria')
  maria = Pessoa(andre, nome='Maria')

  for filho in maria.filhos:
      print(filho.nome)

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão.'

class Mutante(Pessoa):
    olhos = 3

marcelo.sobrenome = 'Dos Santos'
del maria.filhos
del marcelo.sobrenome
ricardo = Homem(nome='Ricardo')
print(Pessoa.olhos)
print(andre.__dict__)
print(marcelo.olhos)
print(maria.__dict__)
print(marcelo.__dict__)
print(marcelo.metodo_estatico())
print(Pessoa.metodo_estatico())
print(Pessoa.atributo_de_classe_e_nome(), marcelo.atributo_de_classe_e_nome())
pessoa = Pessoa()
print(isinstance(pessoa, Pessoa))
print(isinstance(ricardo, Pessoa))
print(isinstance(marcelo, Pessoa))
john = Pessoa(nome='John')
wayne = Homem(nome='Wayne')
print(john.cumprimentar())
print(wayne.cumprimentar())


