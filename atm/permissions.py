import jwt
import grpc
from rest_framework.permissions import BasePermission

from protos import authorization_pb2, authorization_pb2_grpc

class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        user_token = str(request.headers.get('Authorization')).split(' ')[1]
        access_token = jwt.decode(user_token, options={"verify_signature": False})
        print(access_token)
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = authorization_pb2_grpc.AuthorizationStub(channel)
            metadata = (('access_token', user_token),)
            response = stub.isCustomer(authorization_pb2.AuthorizationRequest(), metadata=metadata)
            print(response)
            if response.resp == 1:
                return True
            return False
        