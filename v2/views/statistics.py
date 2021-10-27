# DRF
from rest_framework.decorators import api_view
from rest_framework.response import Response
#
from django.shortcuts import render
#
from v2.utils.network import fetch
from v2.config.settings import (
    BANK_IP,
    BANK_PROTOCOL,
    TREASURY_ACCOUNT_NUMBER,
    GOVERNMENT_ACCOUNT_NUMBER
)

@api_view(['GET'])
def treasuryStats(request):
    next_url = (
        f'{BANK_PROTOCOL}://{BANK_IP}/bank_transactions'
        f'?account_number={TREASURY_ACCOUNT_NUMBER}'
        f'&fee=NONE'
    )
    
    while next_url:
        data = fetch(url=next_url, headers={})
        bank_transactions = data['results']
        next_url = data['next']

        transactions = []
        total = 0

        for bank_transaction in bank_transactions:
            try:
                amount = bank_transaction['amount']
                if(amount == 1):
                    continue
                obj = {
                    'transactions' : bank_transaction['amount']
                }
                transactions.append(obj)
                total = total + amount
            except DuplicateKeyError:
                break
        
        response = {
            'total_treasury_withdrawals' : total,
            'transactions' : transactions
        }
    return Response(response)

@api_view(['GET'])
def govtStats(request):
    next_url = (
        f'{BANK_PROTOCOL}://{BANK_IP}/bank_transactions'
        f'?account_number={GOVERNMENT_ACCOUNT_NUMBER}'
        f'&fee=NONE'
        f'&ordering=-block__created_date'
        f'&limit=20'
        f'&offset=20'
    )
    
    while next_url:
        data = fetch(url=next_url, headers={})
        bank_transactions = data['results']
        next_url = data['next']

        total = 0

        for bank_transaction in bank_transactions:
            try:
                amount = bank_transaction['amount']
               
                total = total + amount
            except Exception:
                pass
        
        response = {
            'total_govt_payment' : total,
        }
    return Response(response)

# return Response('message')
# '_id': bank_transaction['id'],
# 'amount': bank_transaction['amount'],
# 'block_id': bank_transaction['block']['id'],
# 'confirmation_checks': 0,
# 'is_confirmed': False,
# 'memo': bank_transaction['memo'],
# 'sender': bank_transaction['block']['sender']