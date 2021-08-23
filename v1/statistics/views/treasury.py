from rest_framework import mixins, viewsets

from ..models.treasury import TreasuryStatistic

from ..serializers.treasury import TreasuryStatisticSerializer


class TreasuryViewSet(mixins.ListModelMixin,
                      viewsets.GenericViewSet):

    queryset = TreasuryStatistic.objects.all()
    serializer_class = TreasuryStatisticSerializer
