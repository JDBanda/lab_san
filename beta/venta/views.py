from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from . import utils
import json
from django.http import JsonResponse, HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .filters import *

# Create your views here.


def menu(request):
    context = {}
    return render(request, 'venta/menu_caja.html', context)

# Navegación registrado


@login_required
def caja(request):
    paciente = Paciente.objects.all()
    modo_pago = modoPago.objects.all()
    status = Status.objects.all()
    medico = Medico.objects.all()
    servicio = Servicio.objects.all()
    context = {
        # Llevaria dos propiedades extra ?? creo no
        'paciente': paciente,
        'modo_pago': modo_pago,
        'status': status,
        'medico': medico,
        'servicio': servicio,
    }
    return render(request, 'venta/caja.html', context)


@login_required
def PacienteList(request):
    paciente = Paciente.objects.all()
    context = {'paciente': paciente}
    return render(request, 'venta/paciente_list.html', context)


@login_required
def MedicoList(request):
    medico = Medico.objects.all()
    context = {'medico': medico}
    return render(request, 'venta/medico_list.html', context)
# Operaciones CRU
# Paciente


@login_required
def CreatePaciente(request):
    form = PacienteForm()
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/caja/paciente')
    context = {'form': form}
    return render(request, 'venta/form.html', context)


@login_required
def UpdatePaciente(request, pk):
    paciente = Paciente.objects.get(id=pk)
    form = PacienteForm(instance=paciente)
    context = {'form': form}
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('/caja/paciente')
    return render(request, 'venta/form.html', context)
# CRU Médico


@login_required
def CreateMedico(request):
    form = MedicoForm()
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/caja/medico')
    context = {'form': form}
    return render(request, 'venta/form.html', context)


@login_required
def UpdateMedico(request, pk):
    medico = Medico.objects.get(id=pk)
    form = MedicoForm(instance=medico)
    context = {'form': form}
    if request.method == 'POST':
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect('/caja/medico')
    return render(request, 'venta/form.html', context)

# Renglón Servicio, va combinado con la nota
# Sigue en fase de pruebas para añadir excepciones y demas cosas


def prueba(request):
    # Si intento encerrar en bloques try me manda la excepción de la fecha
    # if request.method == 'POST':
    # Obteniendo los datos de la nota
    nota_idPaciente = request.POST.get('NotaPaciente')
    # print(nota_idPaciente)
    nota_idUsuario = request.POST.get('NotaUsuario')
    # print(nota_idUsuario)
    nota_fecha = request.POST.get('NotaFecha')
    # print(nota_fecha)
    nota_statusPago = request.POST.get('NotaStatus')
    # print(nota_statusPago)
    nota_modoPago = request.POST.get('NotaModoPago')
    # print(nota_modoPago)
    nota_entrega = request.POST.get('NotaRecibe')
    # print(nota_entrega)
    nota_pago = request.POST.get('NotaPago')
    # print(nota_pago)
    nota_total = request.POST.get('NotaTotal')
    # Decodificar el JSON
    renglones = request.POST.get('renglones')
    # Un arreglo de diccionarios
    renglones = json.loads(renglones)
    # Crear un nuevo registro de la nota
    nuevaNota = NotaDeVenta(
        nota_idPaciente=Paciente.objects.get(id=nota_idPaciente),
        nota_idUsuario=nota_idUsuario,
        nota_fecha=nota_fecha,
        nota_statusPago=Status.objects.get(id=nota_statusPago),
        nota_modoPago=modoPago.objects.get(id=nota_modoPago),
        nota_entrega=nota_entrega,
        nota_pago=nota_pago,
        nota_total=nota_total)
    # Se guarda, solo hay detalles con la fecha que yo ingreso, pero es un detalle muy puntual
    nuevaNota.save()
    # Crear los N regisros de los renglones a partir del id de esta nota
    val = 0
    while val < len(renglones):
        nuevoRenglon = renglonServicio(
            reng_cantidad=renglones[val]["cantidad"],
            reng_idServicio=Servicio.objects.get(
                id=renglones[val]["servicio"]),
            reng_idNotaDeVenta=NotaDeVenta.objects.latest("id"),
            reng_descuento=renglones[val]["descuento"],
            reng_medico=Medico.objects.get(
                id=renglones[val]["medico"]),
            reng_monto=renglones[val]["monto"]
        )
        nuevoRenglon.save()
        val += 1
    mensaje = "Datos guardados"
    # else:
    # mensaje = "No es POST"
    return JsonResponse({
        'content': {
            'mensaje': mensaje,
        }
    })

# Crear PDF de la ultima nota de venta


def render_pdf_view(request):
    obj = NotaDeVenta.objects.latest("id")
    objRenglones = renglonServicio.objects.filter(reng_idNotaDeVenta=obj.id)
    saldo = obj.nota_total - obj.nota_pago
    template_path = 'venta/nota.html'
    context = {
        'nota': obj,
        'renglones': objRenglones,
        'saldo': saldo
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # Si quisieramos descargarlo
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # Para verlo en el navegador
    response['Content-Disposition'] = 'filename="nota.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# Menú reportes de médicos


def menuMedicos(request):
    medicos = Medico.objects.all()
    context = {'medicos': medicos}
    return render(request, 'venta/medico.html', context)


def reporteMedico(request, pk):
    renglon = RenglonFilter(
        request.GET, queryset=renglonServicio.objects.filter(reng_medico=pk))
    medico = Medico.objects.get(id=pk)
    context = {
        'servicio': renglon,
        'medico': medico,
    }
    return render(request, 'venta/reporte_medico.html', context)

def reporteVenta(request):
    notas = NotaFilter(request.GET, queryset=NotaDeVenta.objects.all())
    context = {'notas': notas}
    return render(request, 'venta/reporte_ventas.html', context)