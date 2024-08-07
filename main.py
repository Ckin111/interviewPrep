from algos.bfs import BFS

def main(graph):
    BFS(graph).execute('A')

if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': [],
        'E': ['H', 'I'],
        'F': [],
        'G': ['J'],
        'H': [],
        'I': [],
        'J': []
    }
    main(graph)