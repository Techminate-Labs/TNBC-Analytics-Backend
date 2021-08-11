from rest_framework import serializers

from ..models.team import Team


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        exclude = ('is_active', )
