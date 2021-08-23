from rest_framework import mixins, viewsets

from ..serializers.transaction import TransactionSerializer

from ..models.transactions import Transaction


class TransactionListView(mixins.ListModelMixin,
                          viewsets.GenericViewSet):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
