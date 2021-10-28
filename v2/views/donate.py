from django.shortcuts import render
# DRF
from rest_framework.decorators import api_view
from rest_framework.response import Response
# models
from v2.models.donate import Donate
# repositories
from v2.repositories.baseRepository import getList
# seriializers
from v2.serializers.donate import DonateSerializer

@api_view(['GET'])
def donates(request):
	donates = getList(Donate)
	serializer = DonateSerializer(donates, many=True)
	return Response(serializer.data)