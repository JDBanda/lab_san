# Generated by Django 3.1.7 on 2021-03-25 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medi_apellidoPaterno', models.CharField(max_length=100)),
                ('medi_apellidoMaterno', models.CharField(max_length=100)),
                ('medi_nombre', models.CharField(max_length=250)),
                ('medi_direccion', models.CharField(max_length=250)),
                ('medi_localidad', models.CharField(max_length=100)),
                ('medi_pais', models.CharField(max_length=100)),
                ('medi_estado', models.CharField(max_length=100)),
                ('medi_municipio', models.CharField(max_length=100)),
                ('medi_cp', models.CharField(max_length=10)),
                ('medi_tel1', models.CharField(max_length=10)),
                ('medi_tel2', models.CharField(max_length=10, null=True)),
                ('medi_email', models.CharField(max_length=250, null=True)),
                ('medi_comision', models.FloatField()),
                ('medi_especialidad', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='NotaDeVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota_fecha', models.DateTimeField()),
                ('nota_statusPago', models.CharField(max_length=250)),
                ('nota_entrega', models.CharField(max_length=250)),
                ('nota_idMedico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='venta.medico')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paci_apellidoPaterno', models.CharField(max_length=100)),
                ('paci_apellidoMaterno', models.CharField(max_length=100)),
                ('paci_nombre', models.CharField(max_length=250)),
                ('paci_direccion', models.CharField(max_length=250)),
                ('paci_localidad', models.CharField(max_length=100)),
                ('paci_pais', models.CharField(max_length=100)),
                ('paci_estado', models.CharField(max_length=100)),
                ('paci_municipio', models.CharField(max_length=100)),
                ('paci_cp', models.CharField(max_length=10)),
                ('paci_tel1', models.CharField(max_length=10)),
                ('paci_tel2', models.CharField(max_length=10, null=True)),
                ('paci_email', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serv_nombre', models.CharField(max_length=250)),
                ('serv_categoria', models.CharField(max_length=250)),
                ('serv_precio', models.FloatField()),
                ('serv_iva', models.FloatField()),
                ('serv_codigobarra', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usua_apellidoPaterno', models.CharField(max_length=100)),
                ('usua_apellidoMaterno', models.CharField(max_length=100)),
                ('usua_nombre', models.CharField(max_length=250)),
                ('usua_direccion', models.CharField(max_length=250)),
                ('usua_localidad', models.CharField(max_length=100)),
                ('usua_pais', models.CharField(max_length=100)),
                ('usua_estado', models.CharField(max_length=100)),
                ('usua_municipio', models.CharField(max_length=100)),
                ('usua_cp', models.CharField(max_length=10)),
                ('usua_tel1', models.CharField(max_length=10)),
                ('usua_tel2', models.CharField(max_length=10, null=True)),
                ('usua_email', models.CharField(max_length=100)),
                ('usua_clave', models.CharField(max_length=100)),
                ('usua_tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='renglonServicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reng_cantidad', models.PositiveIntegerField()),
                ('reng_descuento', models.FloatField()),
                ('reng_idNotaDeVenta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='venta.notadeventa')),
                ('reng_idServicio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='venta.servicios')),
            ],
        ),
        migrations.AddField(
            model_name='notadeventa',
            name='nota_idPaciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='venta.paciente'),
        ),
        migrations.AddField(
            model_name='notadeventa',
            name='nota_idUsuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='venta.usuario'),
        ),
    ]