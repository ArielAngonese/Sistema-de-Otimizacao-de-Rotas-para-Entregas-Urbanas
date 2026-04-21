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

# Função para calcular a distância total da rota
def calculate_distance(graph, path):
    total_distance = sum(
        graph[path[i]][path[i + 1]][0]["length"]
        for i in range(len(path) - 1)
    )
    return round(total_distance / 1000, 2)

# Função para calcular o tempo estimado de entrega com base na distância e velocidade média
def calculate_estimated_time(distance_km, speed_kmh=40):
    time_hours = distance_km / speed_kmh
    time_minutes = max(1, round(time_hours * 60))
    return time_minutes