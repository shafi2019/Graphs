"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # if vertex_id not in self.vertices:
        self.vertices[vertex_id] = set()
        # else: 
        #     return "vertex is aready in graphs"

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # if v1 is self.vertices and v2 in self.vertices:
        self.vertices[v1].add(v2)
        # else: 
        #     print("One of there vertices does not exist")
    

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """        
        # if vertex_id in self.vertices:
        return self.vertices[vertex_id] 
        # else:
        #     set()

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()
        queue = Queue()
        queue.enqueue(starting_vertex)

        while queue.size() > 0:
            cur_node = queue.dequeue()
            if cur_node not in visited:
                visited.add(cur_node)
                print(cur_node)

                for neighbor in self.get_neighbors(cur_node):
                    queue.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()

        while stack.size() > 0:
            curr_node = stack.pop()
            if curr_node not in visited:
                print(curr_node)
                visited.add(curr_node)
                for neighbor in self.get_neighbors(curr_node):
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()

        def dft(vertex):
            if vertex in visited:
                return
            else:
                visited.add(vertex)
                print(vertex)

            for neighbor in self.get_neighbors(vertex):
                dft(neighbor)

        dft(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        queue.enqueue([starting_vertex])
        visited = set()

        while queue.size() > 0:
            v = queue.dequeue()

            last_vertex = v[-1]

            if last_vertex in visited:
                continue

            else:
                visited.add(last_vertex)

            for neighbor in self.get_neighbors(last_vertex):
                next_path = v[:]
                next_path.append(neighbor)
            
                if neighbor == destination_vertex:
                    return next_path
                else:
                    queue.enqueue(next_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()

        while stack.size() > 0:
            v = stack.pop()

            last_vertex = v[-1]

            if last_vertex in visited:
                continue
            else:
                visited.add(last_vertex)
            
            for neighbor in self.get_neighbors(last_vertex):
                next_path = v[:]
                next_path.append(neighbor)

                if neighbor == destination_vertex:
                    return next_path
                else:
                    stack.push(next_path)


    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = set()

        def dfs(path):
            last_path = path[-1]

            if last_path in visited:
                return None
            else:
                visited.add(last_path)

            if last_path == destination_vertex:
                return path
            
            for neighbor in self.get_neighbors(last_path):
                next_path = path[:]
                next_path.append(neighbor)

                found = dfs(next_path)

                if found:
                    return found

            return None

        return dfs([starting_vertex])

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

