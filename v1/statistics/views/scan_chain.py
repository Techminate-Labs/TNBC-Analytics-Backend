from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.permissions import IsAdminUser

from ..models.government import GovernmentAccountNumber
from ..models.treasury import TreasuryStatistic

from ..utils.scan_chain import scan_chain


class ChainScan(APIView):

    permission_classes = [IsAdminUser]

    def post(self, request, format=None):

        government_accounts = GovernmentAccountNumber.objects.all()
        treasury_account = TreasuryStatistic.objects.first()

        for account_number in government_accounts:
            scan_chain(account_number.account_number)

        scan_chain(treasury_account.account_number)

        return Response(status=status.HTTP_201_CREATED)
