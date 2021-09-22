import django_filters
from .models.transactions import Transaction


class CustomTransactionFilter(django_filters.FilterSet):

    payment_type = django_filters.CharFilter(field_name='payment_type', method='payment_type_include')

    def payment_type_include(self, queryset, name, value):
        if not value:
            return queryset
        values = ''.join(value.split(' ')).split(',')
        queryset = queryset.filter(payment_type__in=values)
        return queryset

    class Meta:
        model = Transaction
        fields = ('payment_type', 'transaction_type', 'direction', 'github_issue_id', 'amount')
