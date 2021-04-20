import django_filters
from django_filters import DateFilter
from .models import renglonServicio, NotaDeVenta


class RenglonFilter(django_filters.FilterSet):
    class Meta:
        model = renglonServicio
        fields = ['reng_monto', 'reng_idNotaDeVenta', 'reng_descuento']



class NotaFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='nota_fecha', lookup_expr='gte')
    end_date = DateFilter(field_name='nota_fecha', lookup_expr='lte')
    class Meta:
        model = NotaDeVenta
        fields = ['nota_statusPago', 'nota_fecha']
        exclude = ['nota_idUsuario']