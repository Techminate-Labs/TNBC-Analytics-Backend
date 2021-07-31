from rest_framework import mixins, viewsets

from ..models.team import Team
from ..serializers.team import TeamSerializer


class TeamViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):

    queryset = Team.objects.all()
    serializer_class = TeamSerializer
