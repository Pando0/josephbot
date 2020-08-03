from random import randint

class Chatbot():
    def __init__(self, db: object) -> None:
        # Recebe a classe do banco de dados
        self.db = db

        # E põe os dados nessas duas arrays
        self.quests = db.get_data()['quests']
        self.answers = db.get_data()['answers']

    def reply(self, user_input: str) -> str or list:
        # Recebe o input do usuario e verifica se ele esta na array do banco
        # Se sim ele retorna a resposta da mesma posição da pergunta na array
        # Se não ele retorna uma resposta aleatoria e uma indicação de erro com o True
        if user_input in self.quests:
            return self.answers[self.quests.index(user_input)]
        else:
            return [self.answers[randint(0, len(self.answers)-1)], True]

    def add(self, new_quest: str, new_answer: str) -> None:
        # Ele usa a função do banco para adicionar os dados ao banco
        self.db.add_data([[new_quest, new_answer]])
        