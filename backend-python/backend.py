from concurrent import futures
import grpc
import logging

import daphne.server
import sonora.asgi
from asgi_cors import asgi_cors
import asyncio

import accounts_pb2
import accounts_pb2_grpc

class AccountServicer(accounts_pb2_grpc.AccountServiceServicer):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self):
        #self.db = route_guide_resources.read_route_guide_database()
        pass

    def GetFeature(self, request, context):
        feature = get_feature(self.db, request)
        if feature is None:
            return route_guide_pb2.Feature(name="", location=request)
        else:
            return feature

def serve():

    grpc_asgi_app = sonora.asgi.grpcASGI()
    print("app1 {}", grpc_asgi_app)

    server = daphne.server.Server(grpc_asgi_app, ["tcp:port=9000:interface=0.0.0.0"], verbosity=10 )

    grpc_asgi_app = asgi_cors(grpc_asgi_app, allow_all=True)
    print("app2 {}", grpc_asgi_app)

    accounts_pb2_grpc.add_AccountServiceServicer_to_server(
        accounts_pb2_grpc.AccountServiceServicer(), grpc_asgi_app.__wrapped__)
    server.run()

if __name__ == '__main__':
    logging.basicConfig()
    serve()