# Generated by Django 5.1.3 on 2024-11-17 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_factura_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(blank=True, null=True),
        ),
    ]