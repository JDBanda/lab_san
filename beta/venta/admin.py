from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Paciente)
admin.site.register(models.Status)
admin.site.register(models.modoPago)
admin.site.register(models.Servicio)
admin.site.register(models.Medico)
admin.site.register(models.Categoria)
admin.site.register(models.NotaDeVenta)
admin.site.register(models.renglonServicio)
