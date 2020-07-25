import numpy as np

class Database():
    def __init__(self):
        self.data = np.genfromtxt('db/data.csv', delimiter=',', dtype=str)

        self.quests = []
        self.answers = []

    def update(self):
        self.quests = []
        self.answers = []

        for arr in self.data:
            self.quests.append(arr[0])
            self.answers.append(arr[1])

    def get_data(self):
        self.update()
        return {
            'quests':self.quests,
            'answers':self.answers
            }
    def add_data(self, new_data):
        self.data = np.append(self.data, new_data, axis=0)

        np.savetxt('db/data.csv', self.data, fmt='%s', delimiter=',')
        return 0
