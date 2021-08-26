from rest_framework import mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from ..serializers.transaction import TransactionSerializer

from ..models.transactions import Transaction

from ..filters import CustomTransactionFilter


class TransactionListView(mixins.ListModelMixin,
                          viewsets.GenericViewSet):

    queryset = Transaction.objects.all().order_by('txs_sent_at')
    serializer_class = TransactionSerializer

    filter_backends = [DjangoFilterBackend]
    filter_class = CustomTransactionFilter
