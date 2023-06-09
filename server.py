from flask import Flask, request, jsonify
from flask_cors import CORS

import osmnx as ox

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
	return "본 API는 GET 형식 요청을 받지 않습니다."

@app.route('/roadPath', methods=['POST'])
def main():
    requestData = request.json

    location = ((requestData['location'])[0], (requestData['location'])[1])
    graph = ox.graph_from_point(location, dist=(requestData['distance']), network_type='drive')

    node_dict = {node: (data['x'], data['y']) for node, data in graph.nodes(data=True)}
    edge_dict = {(u, v): data for u, v, key, data in graph.edges(keys=True, data=True)}

    geometry_data = {}
    for key in edge_dict.keys():
            if 'geometry' in edge_dict[key]:
                geometry_data['{}-{}'.format(key[0], key[1])] = edge_dict[key]['geometry'].coords[:]

    resultData = {
        "node": node_dict,
        "edge": list(edge_dict.keys()),
        "edge_geometry": geometry_data,
    }

    return jsonify(resultData), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)