from chatbot import Chatbot
from dataorquestrer import Database

class Main():
    def __init__(self):
        self.data = Database()
        self.bot = Chatbot(self.data.get_data())

    def update(self):
        self.data = Database()
        self.bot = Chatbot(self.data.get_data())

    def start(self):
        user_input = str(input('>> '))
        if user_input == 'sair':
            return 1

        answer = self.bot.reply(user_input)
        
        if answer != None:
            print(answer)
        else:
            print(user_input+'?')
            new_answer = str(input('>: '))
            self.data.add_data([[user_input, new_answer]])
            self.update()

main = Main()

while True:
    if main.start() == 1:
        break