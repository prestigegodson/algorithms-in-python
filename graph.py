class Graph:

    def __init__(self):
        self.no_of_nodes = 0
        self.adjacent_list = dict()

    def add_vertex(self, node):

        if not self.adjacent_list.get(node):
            self.adjacent_list[node] = []
            self.no_of_nodes += 1

    def add_edges(self, node1, node2):

        if self.adjacent_list.get(node1) is not None and self.adjacent_list.get(node2) is not None:
            self.adjacent_list.get(node1).append(node2)
            self.adjacent_list.get(node2).append(node1)

    def show_connections(self):

        for key in self.adjacent_list.keys():
            print('{0} -> {1}'.format(key, self.adjacent_list.get(key)))


graph = Graph()
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_vertex(6)
graph.add_edges(3, 1)
graph.add_edges(3, 4)
graph.add_edges(4, 2)
graph.add_edges(4, 5)
graph.add_edges(1, 2)
graph.add_edges(1, 0)
graph.add_edges(0, 2)
graph.add_edges(6, 5)
graph.show_connections()
