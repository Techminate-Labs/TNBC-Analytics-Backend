from django.shortcuts import render
# DRF
from rest_framework.decorators import api_view
from rest_framework.response import Response
# models
from v2.models.profile import Profile
# seriializers
from v2.serializers.profile import ProfileSerializer

@api_view(['GET'])
def profiles(request):
	profiles = Profile.objects.all().order_by('-id')
	serializer = ProfileSerializer(profiles, many=True)
	return Response(serializer.data)