from concurrent import futures
import grpc
import logging

import asyncio

import accounts_pb2
import accounts_pb2_grpc

class AccountServiceServicer(accounts_pb2_grpc.AccountServiceServicer):
    """Provides methods that implement functionality of account server."""

    def __init__(self):
        #self.db = route_guide_resources.read_route_guide_database()
        pass

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        print("Create called")
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AuthenticateByEmailAndPassword(self, request, context):
        """Missing associated documentation comment in .proto file."""
        print("Authenticate called")
        #context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        #context.set_details('Method not implemented!')
        return accounts_pb2.Account(token="cau")

    def ChangePassword(self, request, context):
        """Missing associated documentation comment in .proto file."""
        print("ChangePass called")
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    accounts_pb2_grpc.add_AccountServiceServicer_to_server(
        AccountServiceServicer(), server)
    server.add_insecure_port('[::]:8081')
    server.start()
    print("Server started")
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()