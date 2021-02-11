# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import accounts_pb2 as accounts__pb2


class AccountServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/private.AccountService/Create',
                request_serializer=accounts__pb2.User.SerializeToString,
                response_deserializer=accounts__pb2.User.FromString,
                )
        self.AuthenticateByEmailAndPassword = channel.unary_unary(
                '/private.AccountService/AuthenticateByEmailAndPassword',
                request_serializer=accounts__pb2.User.SerializeToString,
                response_deserializer=accounts__pb2.Account.FromString,
                )
        self.ChangePassword = channel.unary_unary(
                '/private.AccountService/ChangePassword',
                request_serializer=accounts__pb2.User.SerializeToString,
                response_deserializer=accounts__pb2.Nothing.FromString,
                )


class AccountServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AuthenticateByEmailAndPassword(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangePassword(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AccountServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=accounts__pb2.User.FromString,
                    response_serializer=accounts__pb2.User.SerializeToString,
            ),
            'AuthenticateByEmailAndPassword': grpc.unary_unary_rpc_method_handler(
                    servicer.AuthenticateByEmailAndPassword,
                    request_deserializer=accounts__pb2.User.FromString,
                    response_serializer=accounts__pb2.Account.SerializeToString,
            ),
            'ChangePassword': grpc.unary_unary_rpc_method_handler(
                    servicer.ChangePassword,
                    request_deserializer=accounts__pb2.User.FromString,
                    response_serializer=accounts__pb2.Nothing.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'private.AccountService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AccountService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/private.AccountService/Create',
            accounts__pb2.User.SerializeToString,
            accounts__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AuthenticateByEmailAndPassword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/private.AccountService/AuthenticateByEmailAndPassword',
            accounts__pb2.User.SerializeToString,
            accounts__pb2.Account.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChangePassword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/private.AccountService/ChangePassword',
            accounts__pb2.User.SerializeToString,
            accounts__pb2.Nothing.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
