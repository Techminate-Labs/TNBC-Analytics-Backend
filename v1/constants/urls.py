from rest_framework.routers import SimpleRouter

from .views.donate import DonateViewSet
from .views.faq import FAQViewSet
from .views.settings import SettingViewSet
from .views.team import TeamViewSet

router = SimpleRouter(trailing_slash=False)
router.register('donate', DonateViewSet)
router.register('faq', FAQViewSet)
router.register('setting', SettingViewSet)
router.register('team', TeamViewSet)
