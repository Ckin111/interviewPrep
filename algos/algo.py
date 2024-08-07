from abc import ABC, abstractmethod
class Algorithm:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()

    @abstractmethod
    def execute(self):
        pass

    def reset(self):
        # resets the visited nodes set
        self.visited = self.visited.clear()

    def validate_node(self,node):
        # validates if node exists in graph -> True, else False
        if node in self.graph:
            return True
        else:
            return False