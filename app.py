from flask import Flask
from flask_restful import Resource, Api, reqparse
import json

with open("data/DMV.JSON") as dmv_json:
    dmv_data = json.load(dmv_json)

with open("data/VitalRecords.JSON") as vital_json:
    vital_data = json.load(vital_json)

parser = reqparse.RequestParser()


class Links(Resource):
    def get(self):
        parser.add_argument("state")
        parser.add_argument("type")
        args = parser.parse_args()
        if args["type"] == "dmv":
            return dmv_data[args["state"]]
        else:
            return vital_data[args["state"]]


app = Flask(__name__)
api = Api(app)
api.add_resource(Links, "/links/")

if __name__ == "__main__":
    app.run(debug=True)
