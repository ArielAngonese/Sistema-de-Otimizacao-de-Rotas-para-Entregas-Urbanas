import networkx as nx

# Função para calcular a rota mais curta usando o Dijkstra
def calculate_route(graph, origin_node, destination_node):
    path = nx.shortest_path(graph, origin_node, destination_node, weight="length")
    return path