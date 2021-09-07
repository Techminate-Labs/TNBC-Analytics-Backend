from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers

from datetime import timedelta
from django.utils import timezone

from ..models.transactions import Transaction


class TreasuryChart(APIView):

    def get(self, request):

        days = request.query_params.get("days", 7)

        try:
            days = int(days)
        except ValueError:
            error = {"error": "Invalid day format!!"}
            raise serializers.ValidationError(error)

        transactions = Transaction.objects.filter(transaction_type=Transaction.TREASURY,
                                                  txs_sent_at__gt=timezone.now() - timedelta(days=days))

        temp = []
        data = []

        for txs in transactions:
            temp.append(txs.amount)
            temp.append(txs.txs_sent_at)
            data.append(temp)
            temp = []

        data = {
            "data": data
        }

        return Response(data, status=status.HTTP_200_OK)


class GovernmentChart(APIView):
    
    def get(self, request):

        days = request.query_params.get("days", 7)

        try:
            days = int(days)
        except ValueError:
            error = {"error": "Invalid day format!!"}
            raise serializers.ValidationError(error)

        transactions = Transaction.objects.filter(transaction_type=Transaction.GOVERNMENT,
                                                  txs_sent_at__gt=timezone.now() - timedelta(days=days))

        temp = []
        data = []

        for txs in transactions:
            temp.append(txs.amount)
            temp.append(txs.txs_sent_at)
            data.append(temp)
            temp = []

        data = {
            "data": data
        }

        return Response(data, status=status.HTTP_200_OK)


class HomepageChart():
    pass
