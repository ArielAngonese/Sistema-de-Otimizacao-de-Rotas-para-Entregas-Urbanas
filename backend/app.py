from flask import Flask, request, jsonify
from flask_cors import CORS

# Criação da aplicação Flask
app = Flask(__name__)
CORS(app)