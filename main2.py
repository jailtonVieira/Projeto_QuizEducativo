import random

pontuação = 0
reniciar = 0
respostaCerto = "Resposta correta!"
respostaIncorreta = "Resposta incorreta!"
encerrar = "Agradecemos por usar o nosso sistema!"
espaçamento = "---------------------------------------------"

listPerguntas = [

    {"pergunta" : "Qual o maior planeta do sistema solar?",
     "alternativas" : ["1) Terra","2) Marte","3) jupiter", "4) Saturno"],
     "correta" : 2
     },
    {"pergunta" : "Em qual continente fica a Alemnha?",
     "alternativas" : ["1) África" , "2) Europa", "3) Ásia", "4) América"],
     "correta" : 2
    },
    {"pergunta": "Qual é a capital da Alemanha",
     "alternativas" : ["1) Munique" , "2) Zurique" , "3) Hamburgo" , "4) Berlim"],
     "correta" : 4
     },
    {"pergunta" : "Qual o maior oceano?",
     "alternativas" : ["1) Oceano atlântico", "2) Oceano pacifico", "3) Oceano indico" , "4) Oceano artico"],
     "correta" : 2
     },
    {"pergunta" : "O Monte Everest é parte da cadeia de montanhas?",
     "alternativas" : ["1) Pirineus", "2) Alpes", "3) Murovdag", "4) Himalaia"],
     "correta" : 4
     },
    {"pergunta" : "Qual a linha que divide o hesmisfério Sul do Norte?",
     "alternativas" : ["1) Tropico de câncer", "2) Trópico de capricórnio", "3) Linha do equador","4) Linha do meio" ],
     "correta" : 3
    },
    {"pergunta" : "Qual a nacionalidade do Papa Francisco?",
     "alternativas" : ["1) Argentina","2) Alemã", "3) italiana", "4) Brasileira"],
     "correta" : 1
    },
    {
     "pergunta" :"Quem pintou a Mona lisa?",
     "alternativas" : ["1) Pablo Picasso" ,"2) Leonardo da Vinci", "3) Michelangelo" , "4) Vincent van Gogh" ],
     "correta" : 2
     },
    {
     "pergunta" :"Qual banda fez sucesso ao lançar a musica WE ARE THE CHAMPIONS",
     "alternativas" : ["1) Queen", "2) the beatles" , "3) Pink floyd" ,"4) Cold play"],
     "correta" : 1
    },
    {
     "pergunta" : "O coração humano é um?",
     "alternativas" : ["1) Cartilagem","2) Osso","3) Músculo","4) Tendão"],
     "correta" : 3
    }
]

def Menu():
    while True:
        try:
            print("BEM VINDO AO QUIZ EDUCACIONAL")
            voltaMenu = int(input(f"{espaçamento}\n1 - Iniciar Quiz\n2 - Mostrar pontuação\n3 - Sair\nDigite aqui: "))
            if voltaMenu == 1:
                mostrandoQuiz()
                return True
            elif voltaMenu == 2:
                print(f"{espaçamento}\npontuação do jogador {pontuação} ")
                voltarPont = int(input("1 - Para voltar\nDigite aqui: "))
                if voltarPont == 1:
                    Menu()

                return True
            elif voltaMenu == 3 :
                print(encerrar)
                return False

        except ValueError:
            print(f"Você digitou uma letra,preste mais atenção!")


        print(espaçamento)




def mostrandoQuiz():
    global pontuação
    pontuação = 0
    random.shuffle(listPerguntas)

    for i in listPerguntas[:5]:
        print(espaçamento)
        print(i["pergunta"])
        for j in i["alternativas"]:
            print(j)

        resposta = int(input("qual a sua resposta: "))

        if resposta == i["correta"]:
            pontuação += 1
            print(respostaCerto)
        else :
            print(respostaIncorreta)


    print(espaçamento)
    print(f"você terminou o quiz\nPontuação final {pontuação}/5\nObrigado por jogar o nosso jogo")
    print(f"1 - para voltar ao menu\n2 - para encerrar sessão")
    voltaFinal = int(input("Digite aqui: "))
    if voltaFinal == 1:
        Menu()
    else :
        print(encerrar)




















Menu()
