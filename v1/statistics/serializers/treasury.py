from rest_framework import serializers

from ..models.treasury import TreasuryStatistic


class TreasuryStatisticSerializer(serializers.ModelSerializer):

    class Meta:
        model = TreasuryStatistic
        fields = '__all__'
