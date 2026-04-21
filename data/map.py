import osmnx as ox

# Função de geocodificação para converter um endereço em coordenadas geográficas
def geocode_address(address):
    location = ox.geocode(address)
    return location

# Função para carregar o mapa da cidade usando OSMnx
def load_map(city):
    graph = ox.graph_from_place(city, network_type="drive")
    return graph