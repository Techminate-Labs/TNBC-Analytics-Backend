from django.contrib import admin

from .models.donate import Donate
from .models.faq import FaqType, Faq
from .models.profile import Profile
from .models.contributor import Contributor

admin.site.register(FaqType)
admin.site.register(Faq)
admin.site.register(Profile)
admin.site.register(Contributor)
admin.site.register(Donate)
