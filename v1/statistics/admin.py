from django.contrib import admin  # noqa: F401

# Register your models here.
from .models.government import GovernmentAccountNumber, GovernmentStatistic
from .models.treasury import TreasuryStatistic
from .models.transactions import GovernmentTransaction, TreasuryTransaction
from .models.github import GithubIssue
from .models.statistics import Statistic

admin.site.register(GovernmentAccountNumber)
admin.site.register(GovernmentStatistic)
admin.site.register(TreasuryStatistic)
admin.site.register(GovernmentTransaction)
admin.site.register(TreasuryTransaction)
admin.site.register(GithubIssue)
admin.site.register(Statistic)
