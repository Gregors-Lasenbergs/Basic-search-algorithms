import graph
from search import breadth_first_search as BFS
from search import depth_first_search as DFS
from search import uniform_cost_search as UCS


if __name__ == "__main__":

    # Making the graph
    graph_1 = graph.Graph()
    graph_1.add_vertex("A")
    graph_1.add_vertex("B")
    graph_1.add_vertex("C")
    graph_1.add_vertex("D")
    graph_1.add_vertex("E")
    graph_1.add_vertex("F")
    graph_1.add_vertex("G")
    graph_1.add_edge("A", "B", 2, False)
    graph_1.add_edge("A", "C", 1, False)
    graph_1.add_edge("A", "D", 1, False)
    graph_1.add_edge("A", "G", 6, False)
    graph_1.add_edge("D", "F", 1, False)
    graph_1.add_edge("F", "G", 3, False)
    graph_1.add_edge("C", "E", 1, False)
    print(graph_1)

    # Printing all searches
    BFS(graph_1, "B", "G")
    print()
    DFS(graph_1, "B", "G")
    print()
    UCS(graph_1, "B", "G")

