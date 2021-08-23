from rest_framework import mixins, viewsets

from ..models.government import GovernmentStatistic
from ..serializers.government import GovernmentStatisticSerializer


class GovernmentViewSet(mixins.ListModelMixin,
                        viewsets.GenericViewSet):

    queryset = GovernmentStatistic.objects.all()
    serializer_class = GovernmentStatisticSerializer
