from urllib import response
from rest_framework import serializers
import grpc

from protos import card_to_card_pb2, card_to_card_pb2_grpc
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
    
    def create(self, validated_data):
        token = str(self.context['request'].headers.get('Authorization')).split(' ')[1]
        with grpc.insecure_channel('localhost:50052') as channel:
            stub = card_to_card_pb2_grpc.cardToCardStub(channel)
            metadata = (('access_token', token),)
            response = stub.CardToCard(card_to_card_pb2.CardToCardRequest(dest_account_no=validated_data['destination_account_no'],
                                                        amount=validated_data['amount']), metadata=metadata)
        
        if response.status == 201:
            return super().create(validated_data)
        return super().create(validated_data)

class CardToCardSerializer(serializers.Serializer):
    destination_account_no = serializers.CharField()
    amount = serializers.CharField()