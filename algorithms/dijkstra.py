import math

def calculate_route(graph, origin_node, destination_node):
    distances = {node: float("inf") for node in graph.nodes} # Dicionário que inicializa as distâncias como infinito
    distances[origin_node] = 0 
    previous = {node: None for node in graph.nodes} # Dicionário que inicializa todos os nós já visitados como None
    unvisited = set(graph.nodes) # Conjunto com todos os nós do grafo que não foram visitádos ainda

    while unvisited:
        current = min(unvisited, key=lambda node: distances[node]) # Encontra o nó com a menor distância entre os nós não visitados

        if current == destination_node: 
            break

        if distances[current] == float("inf"):
            break

        unvisited.remove(current) # Remove o nó atual do conjunto dos que não foram visitados

        for neighbor in graph.neighbors(current): # Percorre todos os nós visinhos ao atual
            edge_data = graph[current][neighbor][0] # Pega o primeiro dados da aresta entre o nó atual e o vizinho
            weight = edge_data.get("length", 1) # Pega o comprimento da rua em metros
            new_distance = distances[current] + weight # Calcula a distância total passando pelo nó atual até esse vizinho

            if new_distance < distances[neighbor]: # Se a nova distância for menor que anterior, atualiza
                distances[neighbor] = new_distance
                previous[neighbor] = current

    path = [] # Reconstrói o caminho de trás pra frente
    current = destination_node
    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse() 
    return path