from flask import Flask, request, jsonify, send_file
from flask_restful import Resource, Api
from manual_detection import detect_corals_in_image, red_ring_image
import cv2
import numpy as np

app = Flask(__name__)
api = Api(app)

todos = {"id": "hello"}

global_size = 0
@app.route("/img", methods=["POST"])
def process_image():
    global global_size
    print(request.files["image"])
    file = request.files["image"]
    file.save("image_file.png")
    # Read the image via file.stream
    img = cv2.imread("image_file.png")
    image, size = red_ring_image(img)
    global_size = size

    cv2.imwrite("edited_file.png", image)


    return send_file("edited_file.png", mimetype="image/gif")

@app.route("/size", methods=["GET"])
def get_size():
    return jsonify(np.int(global_size))


if __name__ == "__main__":
    app.run(debug=True)
