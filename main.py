from flask import Flask, request, jsonify
from flask_cors import CORS
import json import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, methods=["POST"])

@app.route("/metrics", methods=["POST"])
def metrics():
  data = request.get_json()

  regions = data.get("regions", [])
  threshold = data.get("threshold_ms", 180)

  with open("q-vercel-latency.json", "r") as f:
    regions_data = json.load(f).get("regions", [])

  result = []
  for region in regions:
    matches = [obj for obj in regions_data if obj.get("region") == region]
    result.append(matches[0])

  return jsonify(result)

app.run(debug=True)
