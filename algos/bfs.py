from .algo import Algorithm

class BFS(Algorithm):
    def __init__(self,graph):
        super().__init__(graph)

    def execute(self,start_node):
        print(self.validate_node(start_node))
        self.visited.add(start_node)
        print(self.visited)
        self.reset()
        print(self.visited)
    