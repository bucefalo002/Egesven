# Generated by Django 5.0.4 on 2024-12-10 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='rol',
            field=models.IntegerField(choices=[(1, 'Administrativo'), (2, 'Cliente')], default=2),
        ),
    ]
