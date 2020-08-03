from chatbot import Chatbot
from dataorquestrer import Database
from time import sleep

class Main():
    def __init__(self) -> None:
        # Configurando o chatbot
        self.update()
        
    def update(self) -> None:
        # Criando os objetos do bot
        self.data = Database()
        self.bot = Chatbot(self.data)

    def start(self) -> None or int:
        # Função principal do loop:

        # Pega o input do usuario e verifica a decisao de saida
        user_input = str(input('>> '))
        if user_input == 'sair':
            return 1

        # Pegando a resposta vinda do bot
        answer = self.bot.reply(user_input)

        # Verificando se o bot realmente achou a resposta
        # Se sim ele retornara uma string com a resposta
        # Se não ele retorna uma lista com uma resposta aleatoria e com a ultima posisão True
        if answer[-1] != True:
            print(answer)
        else:
            print(answer[0])
            sleep(1)
            print(user_input+'?')

            # Adicionando a nova pergunta ao banco e atualizando os dados
            self.bot.add(user_input, str(input('>> ')))
            self.update()

main = Main()

while True:
    if main.start() == 1:
        print('flws')
        break