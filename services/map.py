import osmnx as ox

# Função de geocodificação para converter um endereço em coordenadas geográficas
def geocode_address(address):
    location = ox.geocode(address)
    return location

# Função para carregar o mapa da cidade usando OSMnx
def load_map(city):
    graph = ox.graph_from_place(city, network_type="drive")
    return graph

# Função para encontrar o nó mais próximo no grafo
def get_nearest_node(graph, latitude, longitude):
    node = ox.nearest_nodes(graph, longitude, latitude)
    return node

# Função para calcular a rota mais curta usando o Dijkstra
def get_route_coordinates(graph, path):
    coordinates = []
    for node in path:
        point = graph.nodes[node]
        coordinates.append((point["y"], point["x"]))
    return coordinates