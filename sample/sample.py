from flask import Flask, jsonify
from frame import FlaskGRPC

from sample.company_pb2_grpc import CompanyServerStub
from google.protobuf.empty_pb2 import Empty

app = Flask(__name__)
flask_grpc = FlaskGRPC(app)

flask_grpc.register("company_connection", host="localhost", port=9100)


@app.route("/company")
def get_all_company():
    stub = flask_grpc.company_connection.get_stub(CompanyServerStub)
    result = stub.GetAllCompany(Empty())
    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
