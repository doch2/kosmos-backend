from flask import Flask, request, jsonify
from flask_cors import CORS

import osmnx as ox

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
	return "본 API는 GET 형식 요청을 받지 않습니다."

@app.route('/roadPath', methods=['GET'])
def main():
    requestData = request.json

    location = ((requestData['location'])[0], (requestData['location'])[1])
    graph = ox.graph_from_point(location, dist=500, network_type='all')

    node_dict = {node: (data['x'], data['y']) for node, data in graph.nodes(data=True)}
    resultData = list(node_dict.values())

    return jsonify({"result": resultData}), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)