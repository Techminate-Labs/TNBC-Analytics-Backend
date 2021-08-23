from rest_framework import mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from ..serializers.transaction import TransactionSerializer

from ..models.transactions import Transaction


class TransactionListView(mixins.ListModelMixin,
                          viewsets.GenericViewSet):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['transaction_type']