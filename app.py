from flask import Flask
from flask_restful import Resource, Api, reqparse
import json

with open("data/DMV.JSON") as dmv_json:
    dmv_data = json.load(dmv_json)

with open("data/VitalRecords.JSON") as vital_json:
    vital_data = json.load(vital_json)

parser = reqparse.RequestParser()


class Vital_Records(Resource):
    def get(self):
        parser.add_argument("state")
        args = parser.parse_args()
        return vital_data[args["state"]]


class DMV(Resource):
    def get(self):
        parser.add_argument("state")
        args = parser.parse_args()
        return dmv_data[args["state"]]


app = Flask(__name__)
api = Api(app)
api.add_resource(Vital_Records, "/get_url/vital_records/")
api.add_resource(DMV, "/get_url/state_id/")

if __name__ == "__main__":
    app.run(debug=True)
