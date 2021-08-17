from rest_framework import mixins, viewsets

from ..models.donate import Donate
from ..serializers.donate import DonateSerializer

from v1.statistics.utils.scan_chain import check_confirmation


class DonateViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    queryset = Donate.objects.filter(is_active=True)
    serializer_class = DonateSerializer
