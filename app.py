from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Libera CORS para todas as origens (apenas para desenvolvimento/testes)

API_BASE_URL = "https://api-dados-abertos.tce.ce.gov.br/"

@app.route('/proxy/<metodo>', methods=['GET'])
def proxy(metodo):
    params = request.args.to_dict()
    url = f"{API_BASE_URL}{metodo}"

    try:
        resp = requests.get(url, params=params, timeout=30)
        resp.raise_for_status()
        return jsonify(resp.json()), resp.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
