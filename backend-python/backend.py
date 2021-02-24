from concurrent import futures
import grpc
import logging

import asyncio

import accounts_pb2
import accounts_pb2_grpc
import todo_pb2
import todo_pb2_grpc

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

class TodoServiceServicer(todo_pb2_grpc.TodoServiceServicer):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        print("Create todo called")
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        print("Delete todo called")
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTodos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        print("List todo called")
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    accounts_pb2_grpc.add_AccountServiceServicer_to_server(
        AccountServiceServicer(), server)
    todo_pb2_grpc.add_TodoServiceServicer_to_server(
        TodoServiceServicer, server)

    server.add_insecure_port('[::]:8081')
    server.start()
    print("Server started")
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()