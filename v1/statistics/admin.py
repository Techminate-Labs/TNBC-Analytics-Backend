from django.contrib import admin  # noqa: F401

# Register your models here.
from .models.government import GovernmentAccountNumber, GovernmentStatistic
from .models.treasury import TreasuryStatistic
from .models.transactions import Transaction
from .models.statistics import Statistic
from .models.scan_tracker import ScanTracker

class TransactionAdmin(admin.ModelAdmin):
    search_fields = ('amount',)

admin.site.register(GovernmentAccountNumber)
admin.site.register(GovernmentStatistic)
admin.site.register(TreasuryStatistic)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Statistic)
admin.site.register(ScanTracker)

