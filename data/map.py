import osmnx as ox

def geocode_address(address):
    location = ox.geocode(address)
    return location