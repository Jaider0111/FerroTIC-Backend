# Generated by Django 3.2.8 on 2021-10-09 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ferroticApp', '0003_alter_usuario_ubicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='codigo',
            field=models.BigIntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fotoPerfil',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='numeroDocumento',
            field=models.BigIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='ubicacion',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to='ferroticApp.ubicacion'),
        ),
    ]
