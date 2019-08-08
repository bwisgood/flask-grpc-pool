# Abstract

This project is used for flask app send grpc request, achieve a connection pool manager to manage your grpc-client-pool, and it simplify call for a connection or a stub method

# Quick Start

1. make a flask instance
`app = Flask(__name__)`
2. initialize FlaskGRPCPool
`flask_grpc = FLaskGRPCPoll(app)`
3. register your connection pool `flask_grpc.register("company_connection", host="localhost", port=9100)`
4. use `flask.company_connection` to get target connection pool
