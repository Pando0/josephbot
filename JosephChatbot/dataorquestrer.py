import numpy as np

class Database():
    def __init__(self) -> None:
        # Pega os dados do arquivo csv
        self.data = np.genfromtxt('db/data.csv', delimiter=',', dtype=str)
        
        self.update()

    def update(self) -> None:
        # Pega os dados coletados do arquivo e separa em duas arrays
        self.quests = []
        self.answers = []

        for arr in self.data:
            self.quests.append(arr[0])
            self.answers.append(arr[1])

    def get_data(self) -> dict:
        # Atualiza as variaveis e retorna elas
        self.update()
        return {
            'quests':self.quests,
            'answers':self.answers
            }
    def add_data(self, new_data: list) -> None:
        # Recebe uma array com os dados, coloca na array principal e salva no arquivo
        self.data = np.append(self.data, new_data, axis=0)
        np.savetxt('db/data.csv', self.data, fmt='%s', delimiter=',')
        