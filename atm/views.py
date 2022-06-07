from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import TransactionSerializer, CardToCardSerializer
from .models import Transaction
from .permissions import IsCustomer

class CardToCardViewSet(ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    permission_classes = [IsCustomer]

    def create(self, request, *args, **kwargs):
        serializer = CardToCardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        source_account_id = "1111"
        destination_account_no = serializer.validated_data['destination_account_no']
        amount = serializer.validated_data['amount']
        data = {'source_account_id': source_account_id, 'destination_account_no': destination_account_no, 'amount': amount}

        transaction_serializer = TransactionSerializer(data=data, context={'request': request})
        transaction_serializer.is_valid(raise_exception=True)
        transaction_serializer.save()

        return Response(transaction_serializer.data, status=status.HTTP_201_CREATED)