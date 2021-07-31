from rest_framework import serializers

from ..models.faq import FAQ


class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQ
        field = '__all__'
