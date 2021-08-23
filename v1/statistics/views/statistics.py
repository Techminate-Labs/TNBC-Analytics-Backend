from rest_framework import mixins, viewsets

from ..models.statistics import Statistic
from ..serializers.statistics import StatisticSerializer


class StatisticsViewSet(mixins.ListModelMixin,
                        viewsets.GenericViewSet):

    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer
