import random
from Perguntas import listPerguntasCM , listPerguntasCP
from Pessoa import jogador

Pessoa = None
pontuaçãoAtual = 0
pontuaçãoCM = 0
pontuaçãoCP = 0
quantQuizesCM = 0
quantQuizesCP = 0
reniciar = 0
respostaCerto = "Resposta correta!"
respostaIncorreta = "Resposta incorreta!"
encerrar = "Agradecemos por usar o nosso sistema!"
espaçamento = "---------------------------------------------"


def Cadastro():
    global Pessoa
    print(espaçamento)
    print(f"Essa é a tela de cadastro do jogador!")
    nome = str(input("Qual o seu nome:"))
    Pessoa = jogador(nome)
    Pessoa.apresentar()
    print(f"{espaçamento}")
    Menu()



def Menu():
        try:
            print("BEM VINDO AO QUIZ EDUCACIONAL")
            voltaMenu = int(input(f"{espaçamento}\n1 - Iniciar Quiz\n2 - Perfil\n3 - Ranking\n3 - Sair\nDigite aqui: "))
            if voltaMenu == 1:
                Escolha()

            elif voltaMenu == 2:
               Perfil()

            elif voltaMenu == 3 :
                print(encerrar)

        except ValueError:
            print(f"Você digitou uma letra,preste mais atenção!")
            Menu()

        print(espaçamento)

def Escolha():
    voltaQ = int(input(f"Antes de iniciar o quiz, você deve escolher qual quer fazer:\n1 - Quiz sobre Ciências naturais e Matematica\n2 - Quiz sobre Ciêcias socias e Português\nDigite aqui:"))
    if voltaQ == 1:
        QuizCM()
    elif voltaQ == 2:
        QuizCP()


def Perfil():
    global pontuaçãoAtual , pontuaçãoCM , pontuaçãoCP , pontoTotal
    global quizesTOtal , quantQuizesCM , quantQuizesCP
    global Pessoa

    quizesTOtal = quantQuizesCM + quantQuizesCP
    pontoTotal = pontuaçãoCP + pontuaçãoCM

    print(f"{espaçamento}\nperfil\nJOGADOR:")
    Pessoa.exibir()
    print(espaçamento)
    print(f"{pontuaçãoAtual} - Pontos do jogo mas recente")
    print(f"{pontuaçãoCM} - pontos perguntas Ciência naturais e Matematica")
    print(f"{pontuaçãoCP} - Pontos perguntas Ciência sociais e Português")
    print(f"{pontoTotal} - total de pontos")
    print(f"{quantQuizesCM} - Quizes Ciência naturais e Matematica")
    print(f"{quantQuizesCP} - Quizes Ciência sociais e Português")
    print(f"{quizesTOtal} - Total de quizes jogados")
    print(espaçamento)
    Menu()

def QuizCM():
    global pontuaçãoAtual
    global pontuaçãoCM
    global quantQuizesCM
    pontuaçãoAtual = 0
    quantQuizesCM += 1
    random.shuffle(listPerguntasCM)

    for i in listPerguntasCM[:10]:
        print(espaçamento)
        print(i["pergunta"])
        for j in i["alternativas"]:
            print(j)

        resposta = int(input("qual a sua resposta: "))

        if resposta == i["correta"]:
            pontuaçãoAtual += 1
            pontuaçãoCM += 1
            print(respostaCerto)
        else :
            print(respostaIncorreta)


    print(espaçamento)
    print(f"você terminou o quiz\nPontuação final {pontuaçãoAtual}/10\nObrigado por jogar o nosso jogo")
    print(f"1 - para voltar ao menu\n2 - para encerrar sessão")
    voltaFinal = int(input("Digite aqui: "))
    if voltaFinal == 1:
        Menu()
    else :
        print(encerrar)

def QuizCP():
    global pontuaçãoAtual
    global pontuaçãoCP
    global quantQuizesCP
    pontuaçãoAtual = 0
    quantQuizesCP += 1
    random.shuffle(listPerguntasCP)

    for i in listPerguntasCP[:10]:

        print(espaçamento)
        print(i["pergunta"])
        for j in i["alternativas"]:
            print(j)

        resposta = int(input("qual a sua resposta: "))

        if resposta == i["correta"]:
            pontuaçãoAtual += 1
            pontuaçãoCP += 1
            print(respostaCerto)
        else :
            print(respostaIncorreta)


    print(espaçamento)
    print(f"você terminou o quiz\nPontuação final {pontuaçãoAtual}/10\nObrigado por jogar o nosso jogo")
    print(f"1 - para voltar ao menu\n2 - para encerrar sessão")
    voltaFinal = int(input("Digite aqui: "))
    if voltaFinal == 1:
        Menu()
    else :
        print(encerrar)

Cadastro()
