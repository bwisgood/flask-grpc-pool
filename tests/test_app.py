from grpc_client_pool.client import ClientConnectionPool


def test_state(app):
    assert app.config["TESTING"] is True
    assert app.extensions.get("grpc-pool") is not None


def test_register(app):
    flask_grpc = app.extensions.get("grpc-pool")
    flask_grpc.register("company_connection", host="localhost", port=9100)
    assert isinstance(flask_grpc.connection_pools.get("company_connection"), ClientConnectionPool)


def test_get_conn(app):
    flask_grpc = app.extensions.get("grpc-pool")
    flask_grpc.register("company_connection", host="localhost", port=9100)
    conn = flask_grpc.company_connection
    assert isinstance(conn, ClientConnectionPool)


def test_send_rpc(client):
    resp = client.get("/company")
    assert resp.status_code == 200
    assert resp.data.decode() == "ok"
