class Chatbot():
    def __init__(self, db):
        self.quests = db['quests']
        self.answers = db['answers']

    def reply(self, user_input):
        if user_input in self.quests:
            return self.answers[self.quests.index(user_input)]
        else:
            return None