from flask import Flask, request, jsonify
import os
from prediction import getAgeGender

app = Flask(__name__)

# mediaDir = "./static/uploaded/"
# member api route
# pip install -r .\requirements.txt


@app.route("/", methods=['GET'])
def root():
    return jsonify(
        message="Age and Gender"
    )


@app.route("/predict", methods=['POST'])
def predict():
    f = request.files['upload']
    if f.filename != "":
        # uploaded_file_path = "uploaded/"+f.filename
        # f.save(image_path)
        age, gender = getAgeGender(f)
        return jsonify(
            age=age,
            gender=gender
        )
        # return "hi"


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
