import networkx as nx

def calcular_rota(grafo, origem, destino):
    try:
        caminho = nx.shortest_path(grafo, origem, destino, weight="length")
        return caminho
    except:
        return None