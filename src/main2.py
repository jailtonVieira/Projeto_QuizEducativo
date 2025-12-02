import random
from Perguntas import listPerguntasCM, listPerguntasCP
from Pessoa import Jogador


jogadorAtual = None

def Cadastro():
    global jogadorAtual
    print("---------------------------------------------")
    print("Tela de criação do jogador")
    nome = input("Digite seu nome: ")
    jogadorAtual = Jogador(nome)
    jogadorAtual.apresentar()
    Menu()


def Menu():
    print("---------------------------------------------")
    print("BEM VINDO AO QUIZ EDUCACIONAL")

    try:
        print("---------------------------------------------")
        opcMenu = int(input("1 - Iniciar Quiz\n2 - Perfil\n3 - Novo jogador\n4 - Sair\nDigite aqui: "))

        if opcMenu == 1:
            Escolha()
        elif opcMenu == 2:
            Perfil()
        elif opcMenu == 3:
            Cadastro()
        elif opcMenu == 4:
            print("Agradecemos por usar o nosso sistema!")
            return
        else:
            print("Opção inválida!")
            Menu()

    except ValueError:
        print("Você digitou uma letra! Tente novamente.")
        Menu()


def Escolha():
    try:
        print("---------------------------------------------")
        opcQuiz = int(input("Antes de iniciar o quiz, escolha qual deseja fazer:\n1 - Ciências Naturais e Matemática\n2 - Ciências Sociais e Português\nDigite aqui: "))
        
        if opcQuiz == 1:
            QuizCM()
        elif opcQuiz == 2:
            QuizCP()
        else:
            print("Opção inválida!")
            Escolha()

    except ValueError:
        print("Digite apenas números!")
        Escolha()


def Perfil():
    print("---------------------------------------------")
    print("PERFIL DO JOGADOR")
    jogadorAtual.exibir()
    Menu()


def QuizCM():
    jogadorAtual.pontuacaoAtual = 0
    jogadorAtual.quantQuizesCM += 1

    random.shuffle(listPerguntasCM)

    for p in listPerguntasCM[:10]:
        print("---------------------------------------------")
        print(p["pergunta"])
        for alt in p["alternativas"]:
            print(alt)

        resposta = int(input("Qual a sua resposta: "))
        if resposta == p["correta"]:
            jogadorAtual.pontuacaoAtual += 1
            jogadorAtual.pontuacaoCM += 1
            print("Resposta correta!")
        else:
            print("Resposta incorreta!")

    print("---------------------------------------------")
    print(f"Você terminou o quiz!\nPontuação final: {jogadorAtual.pontuacaoAtual}/10")
    FinalQuiz()

def QuizCP():
    jogadorAtual.pontuacaoAtual = 0
    jogadorAtual.quantQuizesCP += 1

    random.shuffle(listPerguntasCP)

    for p in listPerguntasCP[:10]:
        print("---------------------------------------------")
        print(p["pergunta"])
        for alt in p["alternativas"]:
            print(alt)

        resposta = int(input("Qual a sua resposta: "))
        if resposta == p["correta"]:
            jogadorAtual.pontuacaoAtual += 1
            jogadorAtual.pontuacaoCP += 1
            print("Resposta correta!")
        else:
            print("Resposta incorreta!")

    print("---------------------------------------------")
    print(f"Você terminou o quiz!\nPontuação final: {jogadorAtual.pontuacaoAtual}/10")
    FinalQuiz()


def FinalQuiz():
    try:
        fim = int(input("1 - Voltar ao menu\n2 - Encerrar sessão\nDigite aqui: "))
        if fim == 1:
            Menu()
        else:
            print("Agradecemos por usar o nosso sistema!")
    except ValueError:
        print("Opção inválida!")
        FinalQuiz()

Cadastro()
