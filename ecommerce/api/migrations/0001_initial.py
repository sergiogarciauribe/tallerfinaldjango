# Generated by Django 5.1.3 on 2024-11-06 00:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarritoCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje_descuento', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('documento', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=200)),
                ('correo', models.EmailField(max_length=254)),
                ('metodo_pago', models.CharField(max_length=50)),
                ('id_trabajador', models.CharField(max_length=50)),
                ('fecha_vinculacion', models.DateField()),
                ('carrito_compra', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.carritocompra')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('documento', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=200)),
                ('correo', models.EmailField(max_length=254)),
                ('metodo_pago', models.CharField(max_length=50)),
                ('id_cliente', models.CharField(max_length=50)),
                ('carrito_compra', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.carritocompra')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]