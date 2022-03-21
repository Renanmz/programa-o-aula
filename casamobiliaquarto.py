from numpy import append


class Quarto:
    def __init__(self, nome, dimensoes):
        self.nome = nome
        self.dimensoes = dimensoes
    def __str__(self):
        return self.nome
        "," + self.dimensoes
class Mobilia:
    def __init__(self, nome, funcao, material, quarto):
        self.nome = nome
        self.funcao = funcao
        self.material = material
        self.quarto = quarto
    
    def __str__(self):
        s = self.nome + "," + self.funcao + "," + self.material
        if self.quarto:
            s += str(self.quarto)
            return s

class Casa:
    def __init__(self, formato, quartos):
        self.formato = formato

        for q in self.quartos:
            s += "," + str(q)
            return s
        if quartos is None:
            raise Exception("Casa precisa de quartos")
        self.quartos = quartos



quarto = Quarto
mobilia = Mobilia
casa = Casa

qtdequartos = int(input("quantidade de quartos = "))
quartos = []
mobilias = []
nu = 0
for i in (0, qtdequartos):

    quarto.nome = input("Nome = ")
    quarto.dimensoes = input("Dimensoes = ")
    q1 = Quarto(nome = quarto.nome, dimensoes = quarto.dimensoes)
    quartos.append(q1)

for j in (0, quartos):
    qtdemobilia = int(input("quantidade de mobilia do quarto", j))
    for k in (0, qtdemobilia):
        nu += 1
        print("mobilia", nu, " do quarto", j)
        mobilia.nome = input("nome = ")
        mobilia.funcao = input("funcao = ")
        mobilia.material = input("material = ")
        m1 = Mobilia(nome = mobilia.nome, funcao = mobilia.funcao, material = mobilia.material, quarto = j)
        mobilias.append(m1)

casa.formato = input("formato da casa = ")
casa.quartos = quartos


c1 = Casa(formato = casa.formato, quartos = casa.quartos)

print(c1)