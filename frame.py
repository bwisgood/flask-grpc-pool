from grpc_client_pool.client import ClientConnectionPool


class FlaskGRPCPool(object):
    """
    初始化程序时使用的类，用来写内部需要的一些app的runtime variable
    """

    connection_pools = {}

    def __init__(self, app=None, **kwargs):
        self.app = app
        # self.ApiView = None
        # self.use_pool = kwargs.pop("use_pool", None)
        if app is not None:
            self.init_app(app, **kwargs)

    def init_app(self, app, **kwargs):
        self.app = app
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['grpc-pool'] = self

    def register(self, name, host, port, pool_size=5, intercept=None, **kwargs):
        if not name:
            raise ValueError("pool must have a name")
        pool = ClientConnectionPool(host, port, pool_size, intercept, **kwargs)
        self.connection_pools[name] = pool

    def __getattr__(self, item):
        pool = self.connection_pools.get(item)
        if not pool:
            raise AttributeError
        return pool
