from rest_framework import mixins, viewsets

from ..models.settings import Setting
from ..serializers.settings import SettingSerializer


class SettingViewSet(mixins.ListModelMixin,
                     viewsets.GenericViewSet):

    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
