from .algo import Algorithm

class BFS(Algorithm):
    def __init__(self,graph):
        super().__init__(graph)

    def execute(self):
        print('hello execute')