from rest_framework import serializers

from ..models.government import GovernmentStatistic


class GovernmentStatisticSerializer(serializers.ModelSerializer):

    class Meta:
        model = GovernmentStatistic
        fields = '__all__'
