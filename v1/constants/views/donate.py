from rest_framework import mixins, viewsets

from ..models.donate import Donate
from ..serializers.donate import DonateSerializer


class DonateViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    queryset = Donate.objects.all()
    serializer_class = DonateSerializer
