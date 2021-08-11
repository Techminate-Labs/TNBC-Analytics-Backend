from rest_framework import mixins, viewsets

from ..models.faq import FAQ
from ..serializers.faq import FAQSerializer


class FAQViewSet(mixins.ListModelMixin,
                 viewsets.GenericViewSet):

    queryset = FAQ.objects.filter(is_active=True)
    serializer_class = FAQSerializer
