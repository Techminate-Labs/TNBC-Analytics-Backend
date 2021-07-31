from rest_framework import serializers

from ..models.settings import Setting


class SettingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Setting
        fields = '__all__'
