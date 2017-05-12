from flask import Flask
from flask import render_template, redirect, request
from db import get_all_cafes_from_db, init_db
from nearest_cafe import find_nearest_cafe

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main_button():
    return render_template("index.html")

@app.route("/map", methods=["POST"])
def show_map():
    cafes = get_all_cafes_from_db()
    ltd = float(request.form.get("ltd"))
    lng = float(request.form.get("lng"))
    nearest_cafe_result = find_nearest_cafe(cafes, ltd, lng)
    nearest_cafe = nearest_cafe_result["cafe"]
    distance = nearest_cafe_result["distance"]
    return render_template('map.html', 
        cafes=cafes, nearest_cafe=nearest_cafe, distance=distance)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
