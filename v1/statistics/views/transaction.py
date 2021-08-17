from rest_framework import mixins, viewsets

from ..serializers.transaction import TransactionSerializer

from ..models.transactions import Transaction


class TransactionListView(mixins.ListModelMixin,
                          viewsets.GenericViewSet):

    queryset = Transaction.objects.exclude(transaction_status=Transaction.IS_FEE)
    serializer_class = TransactionSerializer
