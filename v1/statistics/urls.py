from rest_framework.routers import SimpleRouter

from .views.transaction import TransactionListView
from .views.government import GovernmentViewSet

router = SimpleRouter(trailing_slash=False)
router.register('transaction', TransactionListView)
router.register('government', GovernmentViewSet)
