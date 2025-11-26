# QUIZ ECUCACIONAL  

## Descrição breve
Esse é um projeto de Quiz. Aqui você testar o seu conhecimento em três niveis de dificuldade e aprender com as perguntas.

# TABELA

| opcçoes | links |
|---------|-------|
| codigo | [Clique aqui](./src/main2.py) |
| UML |                      |
|Diadrama de classe | |
| Lista de RF e RNF | |
|Review Sprint  | |
| Como utilizar o codigo | |

## REQUISITOS FUNCIONAIS:
### Cadastrar Jogador
O sistema deve permitir o cadastro de um novo jogador informando nome, idade e posição.
### Iniciar Quiz
O sistema deve permitir ao jogador iniciar um quiz com perguntas e respostas.
### Pontuação
O sistema deve calcular e registrar a pontuação do jogador de acordo com as respostas corretas.
### Selecionar Dificuldade
O menu deve permitir ao jogador escolher o nível de dificuldade antes de começar o quiz (Fácil, Médio, Difícil).
### Exibir Menu Principal
O sistema deve exibir um menu com as opções disponíveis (jogar, ver ranking, sair, etc.).
### Encerrar o Jogo
O sistema deve permitir que o usuário encerre o programa de forma segura.

## REQUISITOS NÃO FUNCIONAIS:
### Usabilidade
O sistema deve ter uma interface simples e intuitiva (menu textual fácil de entender).
### Desempenho
O quiz deve responder rapidamente às entradas do usuário (sem atrasos perceptíveis).
### Integridade dos Dados
As informações de jogadores e pontuações devem ser armazenadas corretamente durante a execução.
### Portabilidade
O sistema deve ser executável em qualquer ambiente com Python instalado (Windows, Linux, macOS).
### Manutenibilidade
O código deve ser modular, separado em classes.

## REVIEW
No processo de planejamento e criação tive algumas dificuldades em relação a organização e implementação do código, sendo falta de organização e criatividade. mas que pode resolver enquanto planejava, mas ainda com certas dificuldades  em algumas áreas.
Sobre o futuro do projeto, estou pensando em adicionar duas listas de perguntas sendo elas de ciências da natureza com matemática  e ciências sociais e português, para o usuário escolher qual achar mais agradável. E já iremos começar a planejar como fazer o cadastro do jogador para a implementação.

## ESTRUTURA DE DADOS
Estamos usando varis estrututa para auxiliar no processo sendo:
- Tipos primitivos.
- variaveis.
- classes.
- funções.
- listas.
- dicionarios.
- bibliotecas.
- try & except.

## EXPLICAÇÃO DO CODIGO
<img width="999" height="900" alt="Image" src="https://github.com/user-attachments/assets/13b50964-1b25-47a4-aa04-b26367ecc8c8" />

Aqui nos temos as variaveis que estão sendo usadas junto do dicionario com as perguntas, alternativas e a respostas.

<img width="752" height="424" alt="Image" src="https://github.com/user-attachments/assets/5e3d6926-1d6f-44b4-a27d-b6249acdf896" />

Aqui é o menu principal com as opções. onde inicia o quiz, mostrar pontos e sair.
usei a if ELSE e TRY EXCEPT, para controlar as volta e prever erros.

<img width="752" height="424" alt="Image" src="https://github.com/user-attachments/assets/5e3d6926-1d6f-44b4-a27d-b6249acdf896" />

Aqui embaralha as perguntas e mostraa as alternativas para escolher e verifica se a sua resposta estar correta e logo em seguida mostrar a sua pontuação e exibe as opções de voltar ao menu ou encerrar.
usei IF ELSE ,  FOR, e a biblioteca RAMDON ,para embaralhar as perguntas e mostrar elas tela e verificar as repostas e somar a pontuação. 

## UML & DIAGRAMA

<img width="767" height="772" alt="Image" src="https://github.com/user-attachments/assets/3e36779c-b18c-46b0-a8de-381242e91ad6" />

<img width="783" height="470" alt="Image" src="https://github.com/user-attachments/assets/5a6f4c67-d3d5-489d-93c1-3badbfde74d2" />


## papeis do projeto:
SCRUM MASTER: Jailton dos santos vieira filho
