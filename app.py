from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from find_nearest import get_closest_hawker_locations


app = Flask(__name__)
cors = CORS(app)

@app.route("/get_hawker_locations" , methods=['GET'])
def get_hawker_locations():
    latitude = request.args.get("latitude")
    longitude = request.args.get("longitude")
    result = get_closest_hawker_locations(latitude, longitude)

    return jsonify(result)

@app.route('/')
def root():
    return render_template('index.html')

if __name__ == "__main__":
    # here is starting of the development HTTP server
    app.run()