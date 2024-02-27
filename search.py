import queue


def breadth_first_search(used_graph, start_vertex, destination_vertex):
    """
    Performs a breath first search.

    Args:
        used_graph (Graph): graph to search in.
        start_vertex (vertex): starting node.
        destination_vertex (vertex): target node.

    Returns:
        None.

    """
    print("Performing BFS")
    parents = {start_vertex: None}
    to_be_visited = queue.Queue()
    to_be_visited.put(start_vertex)
    already_visited = [start_vertex]

    found = False

    # loops through the graph in a breath search way
    while not found:
        current_vertex = to_be_visited.get()
        print("\tVisiting vertex " + current_vertex)

        # checks if node is reached
        if current_vertex == destination_vertex:
            found = True
            print("\tArrived at destination " + current_vertex)
        else:

            # loops through every layer
            for items in used_graph.get_neighbours(current_vertex):
                if items[0] not in already_visited:
                    print("\t\tAdding to queue vertex " + items[0])
                    already_visited.append(items[0])
                    to_be_visited.put(items[0])
                    parents[items[0]] = current_vertex
                else:
                    pass

    path_vertex = destination_vertex
    path = [path_vertex]

    # finds the path trough parents and prints it
    while parents.get(path_vertex) is not None:
        path.append(parents.get(path_vertex))
        path_vertex = parents.get(path_vertex)
    print("Print: ", end="")
    for vertex in reversed(path):
        if vertex == destination_vertex:
            print(vertex)
        else:
            print(vertex + "->", end="")


def depth_first_search(used_graph, start_vertex, destination_vertex):
    """
    Performs a depth first search.

    Args:
        used_graph (Graph): graph to search in.
        start_vertex (vertex): starting node.
        destination_vertex (vertex): target node.

    Returns:
        None.

    """
    print("Performing DFS")
    parents = {start_vertex: None}
    to_be_visited = queue.LifoQueue()
    to_be_visited.put(start_vertex)
    already_visited = [start_vertex]

    found = False

    # loops through the graph in a depth search way.
    while not found:
        current_vertex = to_be_visited.get()
        print("\tVisiting vertex " + current_vertex)

        # checks if the node is reached
        if current_vertex == destination_vertex:
            found = True
            print("\tArrived at destination " + current_vertex)

        # loops in one branch
        else:
            for items in used_graph.get_neighbours(current_vertex):
                if items[0] not in already_visited:
                    print("\t\tAdding to queue vertex " + items[0])
                    already_visited.append(items[0])
                    to_be_visited.put(items[0])
                    parents[items[0]] = current_vertex
                else:
                    pass

    path_vertex = destination_vertex
    path = [path_vertex]

    # keeps track of the path and prints it
    while parents.get(path_vertex) is not None:
        path.append(parents.get(path_vertex))
        path_vertex = parents.get(path_vertex)
    print("Print: ", end="")
    for vertex in reversed(path):
        if vertex == destination_vertex:
            print(vertex)
        else:
            print(vertex + "->", end="")


def uniform_cost_search(used_graph, start_vertex, destination_vertex):
    """
    Performs uniform cost search

    Args:
        used_graph (Graph): graph to search in.
        start_vertex (vertex): starting node.
        destination_vertex (vertex): target node.

    Returns:
        None.

    """
    print("Performing UCS")
    parents = {start_vertex: None}
    to_be_visited = queue.PriorityQueue()
    to_be_visited.put((-1, start_vertex))
    already_visited = {start_vertex: -1}

    found = False

    # loops through the graph based on the cost
    while not found:
        current_vertex = to_be_visited.get()
        print("\tVisiting vertex " + current_vertex[1])

        # checks if it has found the end node
        if current_vertex[1] == destination_vertex:
            found = True
            print("\tArrived at destination " + current_vertex[1])

        # checks the lowest cost and goes to that node
        else:
            for items in used_graph.get_neighbours(current_vertex[1]):
                if items[0] not in already_visited or (parents.get(current_vertex[1]) is not items[0] and items[1] <
                                                       already_visited.get(items[0])):
                    print("\t\tAdding to queue vertex " + items[0] + " with cost " + str(items[1]))
                    already_visited[items[0]] = items[1]
                    to_be_visited.put((items[1], items[0]))
                    parents[items[0]] = current_vertex[1]
                else:
                    pass

    # keeps track of the path and prints it
    path_vertex = destination_vertex
    path = [path_vertex]
    while parents.get(path_vertex) is not None:
        path.append(parents.get(path_vertex))
        path_vertex = parents.get(path_vertex)
    print("Print: ", end="")
    for vertex in reversed(path):
        if vertex == destination_vertex:
            print(vertex)
        else:
            print(vertex + "->", end="")
