# Generated by Django 3.0.3 on 2020-04-22 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Eventos', '0004_auto_20200422_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localidad',
            name='idAsiento',
        ),
        migrations.AddField(
            model_name='asientos',
            name='idLocalidad',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Eventos.Localidad'),
            preserve_default=False,
        ),
    ]
