from flask import Flask, request
from flask_cors import CORS
from flask import jsonify
from find_nearest import get_closest_hawker_locations


app = Flask(__name__)
cors = CORS(app)


@app.route("/test.py" , methods=['GET'])  # consider to use more elegant URL in your JS
def get_x():
    print("in get method")
    args = request.args
    print(args)
    latitude = request.args.get("latitude")
    longitude = request.args.get("longitude")
    result = get_closest_hawker_locations(latitude, longitude)

    print(result)
    return jsonify(result)

if __name__ == "__main__":
    # here is starting of the development HTTP server
    app.run()