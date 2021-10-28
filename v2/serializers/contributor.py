from rest_framework import serializers

from v2.models.contributor import Contributor

class ContributorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        exclude = ('is_active', )
