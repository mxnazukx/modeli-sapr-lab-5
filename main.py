# function to read graph from file
def read_graph(filename):
    graph = {}
    with open(filename, 'r') as f:
        for line in f:
            nodes = line.strip().split()
            node1, node2 = int(nodes[0]), int(nodes[1])
            if node1 not in graph:
                graph[node1] = set()
            graph[node1].add(node2)
            if node2 not in graph:
                graph[node2] = set()
            graph[node2].add(node1)
    return graph

# function to check if two graphs are isomorphic
def is_isomorphic(graph1, graph2):
    if len(graph1) != len(graph2):
        return False
    nodes1 = sorted(list(graph1.keys()))
    nodes2 = sorted(list(graph2.keys()))
    if nodes1 != nodes2:
        return False
    degrees1 = [len(graph1[node]) for node in nodes1]
    degrees2 = [len(graph2[node]) for node in nodes2]
    if sorted(degrees1) != sorted(degrees2):
        return False
    adj_matrix1 = [[int(node2 in graph1[node1]) for node2 in nodes1] for node1 in nodes1]
    adj_matrix2 = [[int(node2 in graph2[node1]) for node2 in nodes2] for node1 in nodes2]
    for i in range(len(nodes1)):
        for j in range(len(nodes1)):
            if adj_matrix1[i][j] != adj_matrix2[i][j]:
                return False
    return True

# example usage
filename1 = 'graph1.txt'
filename2 = 'graph2.txt'
graph1 = read_graph(filename1)
graph2 = read_graph(filename2)
if is_isomorphic(graph1, graph2):
    print("The two graphs are isomorphic.")
else:
    print("The two graphs are not isomorphic.")