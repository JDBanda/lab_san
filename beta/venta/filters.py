import django_filters
from django_filters import DateFilter
from .models import renglonServicio


class RenglonFilter(django_filters.FilterSet):
    class Meta:
        model = renglonServicio
        fields = ['reng_monto', 'reng_idNotaDeVenta', 'reng_descuento']
