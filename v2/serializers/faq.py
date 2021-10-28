from rest_framework import serializers

from v2.models.faq import Faq

class FaqSerializer(serializers.ModelSerializer):

    class Meta:
        model = Faq
        exclude = ('is_active', )
        depth = 1
