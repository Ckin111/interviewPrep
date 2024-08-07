from algos.bfs import BFS

def main(graph):
    print('hello main')
    BFS(graph).execute()

if __name__ == '__main__':
    print('hello world')
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