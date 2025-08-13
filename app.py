import logging
from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.DEBUG)  # Habilita logs debug

API_BASE_URL = "https://api-dados-abertos.tce.ce.gov.br/"

@app.route('/proxy/<metodo>', methods=['GET'])
def proxy(metodo):
    params = request.args.to_dict()
    url = f"{API_BASE_URL}{metodo}"
    app.logger.debug(f"Requisição proxy para URL: {url} com params: {params}")
    try:
        resp = requests.get(url, params=params, timeout=30)
        app.logger.debug(f"Status code da API: {resp.status_code}")
        app.logger.debug(f"Conteúdo da resposta: {resp.text}")
        resp.raise_for_status()
        return jsonify(resp.json()), resp.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
