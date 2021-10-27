from rest_framework import serializers

from v2.models.donate import Donate


class DonateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Donate
        exclude = ('is_active', )
