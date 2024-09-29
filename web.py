from flask import Flask, request, jsonify, send_file, render_template, abort
import json
from flask_cors import CORS

name = f"{__name__}.py"

app = Flask(__name__)
CORS(app)

@app.errorhandler(404)
def q405(e):
    data = ""
    return data, 404

@app.errorhandler(405)
def q405(e):
    data = ""
    return data, 405

@app.errorhandler(401)
def q401(e):
    data = ""
    return data, 401

@app.errorhandler(403)
def q403(e):
    data = ""
    return data, 403

@app.errorhandler(500)
def q405(e):
    data = {"Message":"An error has occurred."}
    return jsonify(data), 500

@app.route("/", methods=["GET"])
def index():
    return abort(404)

@app.route("/lasertag", methods=["GET"])
def lasertag():
    bot = request.args["bot"]
    if bot != "1":
        return abort(400)
    with open("data.json") as f:
        yay = json.load(f)
    return render_template("bot.html", timer=yay[0]["timer"], blueTeam=yay[0]["blueTeam"], redTeam=yay[0]["redTeam"])

@app.route("/lasertag/1/image", methods=["GET"])
def lasertag_1_image():
    return send_file("image1.png")

def run():
    Port = 20231
    Ip = "0.0.0.0"
    app.run(str(Ip), int(Port), debug=True)

run()