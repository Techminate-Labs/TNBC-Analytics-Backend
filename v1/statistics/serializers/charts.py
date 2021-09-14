from rest_framework import serializers


class ChartSerializer(serializers.Serializer):

    days = serializers.CharField(max_length=4)
