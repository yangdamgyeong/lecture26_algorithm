from collections import deque # deque 정의 왜 안함 
class Graph:
    def __init__(self):
        num_nodes, num_edges = map(int, input().split())
        self.directed = int(input('양방향 여부 (1: 양방향, 0 : 단방향) :'))
        self.graph = [[] for _ in range(num_nodes + 1)] 
        for _ in range(num_edges):
            u, v = map(int, input().split())
            self.graph[u].append(v)
            if self.directed:
                self.graph[v].append(u)

        self.visited = []

    def dfs(self, node):
        print(node, end = '')
        self.visited.append(node)
        for adj_node in self.graph[node]:
            if adj_node not in self.visited:
                self.dfs(adj_node)
    
    def bfs(self, start):
        visited = []
        queue = deque()
        #시작 노드에 대해 작업
        queue.append(start)
        self.visited.append(start)
        print(start, end= '')
        #다음에 방문할 노드찾아서 처리
        # (방문한 적이 없는 인접 노드를 찾을 노드)를 queue에서 가져와서 찾기
        while queue:
            node = queue.popleft()
            for adj_node in self.graph[node]:
                if adj_node not in self.visited:
                    queue.append(adj_node)
                    self.visited.append(adj_node)
                    print(adj_node, end=' ')

if __name__ == '__main__':
    g = Graph(bidirection = False)
    start = int(input('시작 노드 번호 : '))
    g.dfs(start)
    print()
    g.visited
    g.bfs(start)
    print()