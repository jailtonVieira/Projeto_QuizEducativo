class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontuacaoAtual = 0
        self.pontuacaoCM = 0
        self.pontuacaoCP = 0
        self.quantQuizesCM = 0
        self.quantQuizesCP = 0

    @property
    def pontoTotal(self):
        return self.pontuacaoCM + self.pontuacaoCP

    @property
    def quizesTotal(self):
        return self.quantQuizesCM + self.quantQuizesCP

    def apresentar(self):
        print(f"Bem-vindo ao Quiz, {self.nome}!")

    def exibir(self):
        print("---------------------------------------------")
        print(f"Jogador: {self.nome}")
        print(f"Pontos do último quiz: {self.pontuacaoAtual}")
        print(f"Pontos Ciências Naturais e Matemática: {self.pontuacaoCM}")
        print(f"Pontos Ciências Sociais e Português: {self.pontuacaoCP}")
        print(f"Total de pontos: {self.pontoTotal}")
        print(f"Quizzes Ciências Naturais e Matemática: {self.quantQuizesCM}")
        print(f"Quizzes Ciências Sociais e Português: {self.quantQuizesCP}")
        print(f"Total de quizzes feitos: {self.quizesTotal}")
        print("---------------------------------------------")
