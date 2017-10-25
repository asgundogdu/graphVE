from heaper import *
from random import randint


class Graph:  # Note that no checking of loops and multiple edges
    def __init__(self):
        print "Graph created!"
        self.edges = []
        self.vertices = []

    def add_vertices(self, names):
        [self.vertices.append(Vertex(label=name)) for name in names]

    def add_edges(self, edges):
        for v in edges:
            s = self.get_vertex(v[0])
            t = self.get_vertex(v[1])
            Vertex.add_child(s, t)
            self.edges.append([v[0], v[1]])

    def control_add_edge(self, edge):

        if (search(self.vertices_names(), edge[0]) == -1) & \
                (search(self.vertices_names(), edge[1]) == -1):  # If both vertices are not exist
            if edge[0] == edge[1]:  # If the first edge being not in the list is loop
                v = Vertex(label=edge[1])  # {v} - Child
                self.vertices.append(v)
                self.edges.append([v, v])
            else:
                v = Vertex(label=edge[1])  # {v} - Child
                u = Vertex(label=edge[0], child=v)  # {u} - Parent
                self.vertices.append(v)
                self.vertices.append(u)
                self.edges.append([u, v])

        elif (search(self.vertices_names(), edge[0]) != -1) & \
                (search(self.vertices_names(), edge[1]) == -1):  # If only parent vertex is exist
            v = Vertex(label=edge[1])  # {v} - Child
            u = self.get_vertex(edge[0])  # {u} - Parent
            Vertex.add_child(u, v)
            self.vertices.append(v)
            self.edges.append([u, v])

        elif (search(self.vertices_names(), edge[0]) == -1) & \
                (search(self.vertices_names(), edge[1]) != -1):  # If only child vertex is exist
            v = self.get_vertex(edge[1])  # {v} - Child
            u = Vertex(label=edge[0], child=v)  # {u} - Parent
            self.vertices.append(u)
            self.edges.append([u, v])

        elif (search(self.vertices_names(), edge[0]) != -1) & \
                (search(self.vertices_names(), edge[1]) != -1):  # If both vertices are exist
            u = self.get_vertex(edge[0])  # {u} - Parent
            v = self.get_vertex(edge[1])  # {v} - Child
            Vertex.add_child(u, v)
            self.edges.append([u, v])

        vertices = [vertex.name for vertex in self.vertices]
        sorted_vertices = [x for (y, x) in heap_sort(zip(vertices, self.vertices))]
        self.vertices = sorted_vertices

    def vertices_names(self):
        return [vertex.get_name() for vertex in self.vertices]

    def get_vertex(self, label):  # Get vertex by name
        vertices = [vertex.name for vertex in self.vertices]
        return self.vertices[search(vertices, label)]

    def dfs(self, v, visited_nodes, finishes=None, scc=None):  # :Graph, :Vertex, :list
        if not isExist(v.name, visited_nodes):  # Append the current node in visited nodes list
            visited_nodes.append(v.name)
            # print v.name
            if scc is not None:
                scc.append(v.name)
        # Call for all the neighbour vertices of current vertex
        neighbours = v.children
        # neighbour_names = Vertex.get_children_names(v)
        for neighbour in neighbours:
            if not isExist(neighbour.name, visited_nodes):
                self.dfs(neighbour, visited_nodes, finishes, scc)
        if finishes is not None:
            finishes.append(v.name)  # finish times

    def get_finishTimes(self, visited_nodes, finishes):
        self.dfs(self.vertices[randint(0, len(self.vertices) - 1)], visited_nodes, finishes)  # Start from random node
        all_names = self.vertices_names()
        while len(visited_nodes) < len(self.vertices):  # loop finishes when the all nodes are used
            for n in all_names:
                if not isExist(n, visited_nodes):
                    self.dfs(self.get_vertex(n), visited_nodes, finishes)

    def get_scc(self, visited_nodes, finishes, output):
        while finishes:
            n = finishes[-1]
            finishes = finishes[:-1]  # Omit last element
            if not isExist(n, visited_nodes):
                # print "Component"
                scc = []
                self.dfs(self.get_vertex(n), visited_nodes, scc=scc)
                output.append(scc)


class Vertex:
    def __init__(self, label, child=None):
        self.name = label
        self.children = []
        if child is not None:
            self.children.append(child)

    def add_child(self, child):
        self.children.append(child)

    def get_name(self):
        return self.name

    def get_children(self):
        return self.children

    def get_children_names(self):
        return [c.name for c in self.children]
