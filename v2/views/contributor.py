from django.shortcuts import render
# DRF
from rest_framework.decorators import api_view
from rest_framework.response import Response
# models
from v2.models.contributor import Contributor
# seriializers
from v2.serializers.contributor import ContributorSerializer

@api_view(['GET'])
def contributors(request):
	contributors = Contributor.objects.all().order_by('-id')
	serializer = ContributorSerializer(contributors, many=True)
	return Response(serializer.data)