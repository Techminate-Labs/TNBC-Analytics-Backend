from rest_framework.routers import SimpleRouter

from .views.transaction import TransactionListView

router = SimpleRouter(trailing_slash=False)
router.register('transaction', TransactionListView)
