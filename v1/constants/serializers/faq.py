from rest_framework import serializers

from ..models.faq import FAQ


class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQ
        fields = '__all__'
        depth = 1
