from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.menu, name='inicio'),
    path('caja/', views.caja, name='caja'),
    # Paciente
    path('caja/paciente', views.PacienteList, name='paciente_list'),
    path('caja/paciente/registrar', views.CreatePaciente, name='paciente_create'),
    path('caja/paciente/editar/<str:pk>',
         views.UpdatePaciente, name='paciente_edit'),
    # Médico
    path('caja/medico', views.MedicoList, name='medico_list'),
    path('caja/medico/registrar', views.CreateMedico, name='medico_create'),
    path('caja/medico/editar/<str:pk>',
         views.UpdateMedico, name='medico_edit'),
    # Renglon Servicio
    # Prueba
    path('prueba/post', views.prueba, name='prueba'),
    # Prueba pdf
    path('caja/nota/pdf', views.render_pdf_view, name='pdf'),
    # Reportes de médico
    path('reportes/medico/', views.menuMedicos, name='medicos'),
    path('reportes/medico/<str:pk>', views.reporteMedico, name='reporte'),
    # Reporte de vena
    path('reportes/venta/', views.reporteVenta, name='reporte_venta'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)