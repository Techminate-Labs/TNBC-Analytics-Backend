from rest_framework import serializers

from ..models.statistics import Statistic


class StatisticSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statistic
        fields = '__all__'
