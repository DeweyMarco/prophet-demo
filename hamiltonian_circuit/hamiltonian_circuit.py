def hamiltonian_circuit(graph):
    """
    Finds a Hamiltonian circuit in a graph using a backtracking approach.

    Args:
        graph: A dictionary representing the graph, where keys are nodes and
               values are lists of their neighbors.

    Returns:
        A list representing a Hamiltonian circuit, or None if no circuit exists.
    """

    num_nodes = len(graph)
    if num_nodes == 0:
        return None

    def is_safe(node, path, pos):
        if node not in graph: 
            return False

        if node in path:
            return True 

        if pos > 0 and node not in graph[path[pos - 1]]:
            return False  

        return True

    def find_circuit_util(path, pos):
        if pos == num_nodes:
            if path[0] in graph[path[-1]]:  
                return path + [path[0]]  
            else:
                return None

        for node in graph:
            if is_safe(node, path, pos):
                path.append(node)
                result = find_circuit_util(path, pos + 1)
                if result:
                    return result
                path.pop()  

        return None

    start_node = list(graph.keys())[0]  
    path = [start_node]
    return find_circuit_util(path, 1)

# Example usage:
graph = {
    0: [1,2],
    1: [0,2,3],
    2: [0,1,3],
    3: [1,2,4],
    4: [3]
}

circuit = hamiltonian_circuit(graph)
print(f"Hamiltonian circuit for graph: {circuit}")