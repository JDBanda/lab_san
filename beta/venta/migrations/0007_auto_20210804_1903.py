# Generated by Django 3.2.6 on 2021-08-05 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0006_auto_20210402_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sucu_nombre', models.CharField(max_length=100, verbose_name='Nombre de sucursal')),
                ('sucu_especialidad', models.CharField(max_length=100, verbose_name='Especialidad')),
            ],
        ),
        migrations.AlterField(
            model_name='categoria',
            name='cate_nombre',
            field=models.CharField(max_length=100, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='medi_apellidoMaterno',
            field=models.CharField(max_length=30, verbose_name='Apellido materno'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='medi_apellidoPaterno',
            field=models.CharField(max_length=30, verbose_name='Apellido paterno'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='medi_direccion',
            field=models.CharField(max_length=150, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='medi_nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre(s)'),
        ),
        migrations.AlterField(
            model_name='modopago',
            name='modo_nombre',
            field=models.CharField(max_length=150, verbose_name='Modo de pago'),
        ),
        migrations.AlterField(
            model_name='notadeventa',
            name='nota_entrega',
            field=models.CharField(max_length=150, verbose_name='quien recibe'),
        ),
        migrations.AlterField(
            model_name='notadeventa',
            name='nota_idUsuario',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='paci_apellidoMaterno',
            field=models.CharField(max_length=30, verbose_name='Apellido materno'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='paci_apellidoPaterno',
            field=models.CharField(max_length=30, verbose_name='Apellido paterno'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='paci_direccion',
            field=models.CharField(max_length=100, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='paci_nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre(s)'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='serv_codigobarra',
            field=models.CharField(max_length=150, verbose_name='Codigo de barras'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='serv_nombre',
            field=models.CharField(max_length=150, verbose_name='Nombre del servicio'),
        ),
        migrations.AlterField(
            model_name='status',
            name='status_nombre',
            field=models.CharField(max_length=150, verbose_name='Estatus'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usua_apellidoMaterno',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usua_apellidoPaterno',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usua_direccion',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usua_nombre',
            field=models.CharField(max_length=50),
        ),
    ]