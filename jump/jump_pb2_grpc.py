# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import jump_pb2 as jump__pb2


class JumpServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Jump = channel.unary_unary(
                '/jump.JumpService/Jump',
                request_serializer=jump__pb2.JumpReq.SerializeToString,
                response_deserializer=jump__pb2.Response.FromString,
                )


class JumpServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Jump(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_JumpServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Jump': grpc.unary_unary_rpc_method_handler(
                    servicer.Jump,
                    request_deserializer=jump__pb2.JumpReq.FromString,
                    response_serializer=jump__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'jump.JumpService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class JumpService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Jump(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/jump.JumpService/Jump',
            jump__pb2.JumpReq.SerializeToString,
            jump__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
