from JosephV4.dataorquestrer import Database
from JosephV4.chatbot import Chatbot
import bottle

class WebApi():
    def __init__(self):
        self.update()

    def update(self):
        self.data = Database()
        self.bot = Chatbot(self.data)

    def replyer(self, quest):
        answer = self.bot.reply(quest)
        if answer[-1] == True:
            return {'answer':answer[0], 'error':True}
        else:
            return {'answer':answer, 'error':False}

    def add(self, new_quest, new_answer):
        try:
            self.bot.add(new_quest, new_answer)
        except:
            return {'status':'error'}
            
        return {'status':'success'}

    def send_data(self):
        return self.data.get_data()

main = WebApi()

# Rotas:

@bottle.route('/reply/<quest>')
def reply(quest):
    return main.replyer(quest)

@bottle.route('/add/<new_quest>/<new_answer>')
def add(new_quest, new_answer):
    return main.add(new_quest, new_answer)

@bottle.route('/database')
def send_data():
    return main.send_data()


# Hosting
bottle.run(host='localhost', port=3000)