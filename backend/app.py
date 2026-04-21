from flask import Flask, request, jsonify
from flask_cors import CORS
from services.map import load_map, get_nearest_node, get_route_coordinates
from algorithms.dijkstra import calculate_route
from backend.database import get_all_deliveries, get_delivery_by_id, insert_delivery, insert_address, update_delivery_route

# Criação da aplicação Flask
app = Flask(__name__)
CORS(app)

# Rota para obter todas as entregas
@app.route("/deliveries", methods=["GET"])
def get_deliveries():
    deliveries = get_all_deliveries()
    return jsonify(deliveries)

# Rota para obter uma entrega específica por ID
@app.route("/deliveries/<int:id>", methods=["GET"])
def get_delivery(id):
    delivery = get_delivery_by_id(id)
    if delivery is None:
        return jsonify({"erro": "Entrega não encontrada"}), 404
    return jsonify(delivery)

# Rota para criar uma nova entrega
@app.route("/deliveries", methods=["POST"])
def create_delivery():
    data = request.get_json()

    id_origin_address = insert_address(
        data["origin_street"],
        data["origin_number"],
        data["origin_city"],
        data["origin_lat"],
        data["origin_lng"]
    )

    id_destination_address = insert_address(
        data["destination_street"],
        data["destination_number"],
        data["destination_city"],
        data["destination_lat"],
        data["destination_lng"]
    )

    id_delivery = insert_delivery(
        status="pendente",
        data=data["date"],
        id_usuario=data["user_id"],
        id_destinatario=data["recipient_id"],
        id_endereco_origem=id_origin_address,
        id_endereco_destino=id_destination_address
    )

    return jsonify({"delivery_id": id_delivery}), 201

# Rota para calcular a rota mais curta entre origem e destino
@app.route("/calculate-route", methods=["POST"])
def calculate_route_api():
    data = request.get_json()

    origin_lat = data["origin_lat"]
    origin_lng = data["origin_lng"]
    destination_lat = data["destination_lat"]
    destination_lng = data["destination_lng"]

    graph = load_map(data["city"])

    origin_node = get_nearest_node(graph, origin_lat, origin_lng)
    destination_node = get_nearest_node(graph, destination_lat, destination_lng)

    path = calculate_route(graph, origin_node, destination_node)
    coordinates = get_route_coordinates(graph, path)

    if "delivery_id" in data:
        update_delivery_route(
            data["delivery_id"],
            data["distance"],
            data["estimated_time"]
        )

    return jsonify({"route": coordinates})
