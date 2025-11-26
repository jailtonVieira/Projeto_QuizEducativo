class jogador:
    def __init__(self,nome):
        self.nome = nome

    def apresentar(self):
        print(f"Bem vindo {self.nome}")


    def exibir(self):
        print(f"Jogador: {self.nome}")