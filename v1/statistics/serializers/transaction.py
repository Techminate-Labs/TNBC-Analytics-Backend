from rest_framework import serializers

from ..models.transactions import Transaction


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'
