from django.contrib import admin

from .models.donate import Donate
from .models.faq import FAQ, FaqCategory
from .models.settings import Setting
from .models.team import Team

# Register your models here.
admin.site.register(Donate)
admin.site.register(FAQ)
admin.site.register(Setting)
admin.site.register(Team)
admin.site.register(FaqCategory)
