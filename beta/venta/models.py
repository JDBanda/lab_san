from django.db import models

# Create your models here.

# Tablas básicas


class Paciente(models.Model):
    paci_apellidoPaterno = models.CharField("Apellido paterno", max_length=100)
    paci_apellidoMaterno = models.CharField("Apellido materno", max_length=100)
    paci_nombre = models.CharField("Nombre(s)", max_length=250)
    paci_direccion = models.CharField("Dirección", max_length=250)
    paci_localidad = models.CharField("Localidad", max_length=100)
    paci_pais = models.CharField("País", max_length=100)
    paci_estado = models.CharField("Estado", max_length=100)
    paci_municipio = models.CharField("Municipio", max_length=100)
    paci_cp = models.CharField("Código postal", max_length=10)
    paci_tel1 = models.CharField("Teléfono 1", max_length=10)
    paci_tel2 = models.CharField("Teléfono 2", max_length=10, null=True)
    paci_email = models.CharField("Email", max_length=250, null=True)

    def __str__(self):
        return self.paci_apellidoPaterno + " " + self.paci_apellidoMaterno + " " + self.paci_nombre


class Medico(models.Model):
    medi_apellidoPaterno = models.CharField("Apellido paterno", max_length=100)
    medi_apellidoMaterno = models.CharField("Apellido materno", max_length=100)
    medi_nombre = models.CharField("Nombre(s)", max_length=250)
    medi_direccion = models.CharField("Dirección", max_length=250)
    medi_localidad = models.CharField("Localidad", max_length=100)
    medi_pais = models.CharField("País", max_length=100)
    medi_estado = models.CharField("Estado", max_length=100)
    medi_municipio = models.CharField("Municipio", max_length=100)
    medi_cp = models.CharField("Código postal", max_length=10)
    medi_tel1 = models.CharField("Teléfono 1", max_length=10)
    medi_tel2 = models.CharField("Teléfono 2", max_length=10, null=True)
    medi_email = models.CharField("Email", max_length=250, null=True)
    medi_comision = models.FloatField("Comisión")
    medi_especialidad = models.CharField("Especialidad", max_length=150)

    def __str__(self):
        return self.medi_apellidoPaterno + " " + self.medi_apellidoMaterno + " " + self.medi_nombre


class Usuario(models.Model):
    usua_apellidoPaterno = models.CharField(max_length=100)
    usua_apellidoMaterno = models.CharField(max_length=100)
    usua_nombre = models.CharField(max_length=250)
    usua_direccion = models.CharField(max_length=250)
    usua_localidad = models.CharField(max_length=100)
    usua_pais = models.CharField(max_length=100)
    usua_estado = models.CharField(max_length=100)
    usua_municipio = models.CharField(max_length=100)
    usua_cp = models.CharField(max_length=10)
    usua_tel1 = models.CharField(max_length=10)
    usua_tel2 = models.CharField(max_length=10, null=True)
    usua_email = models.CharField(max_length=100)
    usua_clave = models.CharField(max_length=100)
    usua_tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.usua_email


class Categoria(models.Model):
    cate_nombre = models.CharField("Categoria", max_length=250)

    def __str__(self):
        return self.cate_nombre


class modoPago(models.Model):
    modo_nombre = models.CharField("Modo de pago", max_length=250)

    def __str__(self):
        return self.modo_nombre


class Status(models.Model):
    status_nombre = models.CharField("Estatus", max_length=250)

    def __str__(self):
        return self.status_nombre

# tablas compuestas


class Servicio(models.Model):
    serv_nombre = models.CharField("Nombre del servicio", max_length=250)
    serv_categoria = models.ForeignKey(
        Categoria, null=True, on_delete=models.SET_NULL)
    serv_precio = models.FloatField("Precio")
    serv_iva = models.FloatField("IVA")
    serv_codigobarra = models.CharField("Codigo de barras", max_length=250)

    def __str__(self):
        return self.serv_nombre


class NotaDeVenta(models.Model):
    nota_idPaciente = models.ForeignKey(
        Paciente, null=True, on_delete=models.SET_NULL)
    # Pendiente por que no se acceder a los usuarios
    nota_idUsuario = models.CharField(max_length=250, null=True)
    nota_fecha = models.DateTimeField("Fecha")
    nota_statusPago = models.ForeignKey(
        Status, null=True, on_delete=models.SET_NULL)
    nota_modoPago = models.ForeignKey(
        modoPago, null=True, on_delete=models.SET_NULL)
    nota_entrega = models.CharField("quien recibe", max_length=250)
    nota_pago = models.FloatField(null=True)
    nota_total = models.FloatField(null=True)

    def __str__(self):
        return str(self.id) + ": " + self.nota_idPaciente.paci_apellidoPaterno + " " + self.nota_idPaciente.paci_apellidoMaterno + " " + self.nota_idPaciente.paci_nombre


class renglonServicio(models.Model):
    reng_cantidad = models.PositiveIntegerField()
    reng_idServicio = models.ForeignKey(
        Servicio, null=True, on_delete=models.SET_NULL)
    reng_idNotaDeVenta = models.ForeignKey(
        NotaDeVenta, null=True, on_delete=models.SET_NULL)
    reng_descuento = models.FloatField()
    reng_medico = models.ForeignKey(
        Medico, null=True, on_delete=models.SET_NULL)
    reng_monto = models.FloatField(null=True)

    def __str__(self):
        return str(self.reng_idNotaDeVenta.id) + ", " + str(self.id) + ": " + self.reng_idServicio.serv_nombre
