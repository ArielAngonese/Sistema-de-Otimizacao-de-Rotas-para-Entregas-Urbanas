import osmnx as ox

def carregar_mapa(cidade):
    grafo = ox.graph_from_place(cidade, network_type="drive")
    return grafo