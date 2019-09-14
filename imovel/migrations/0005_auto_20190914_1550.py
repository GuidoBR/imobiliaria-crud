# Generated by Django 2.2.5 on 2019-09-14 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imovel', '0004_auto_20181112_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovel',
            name='aluguel',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='imovel',
            name='condominio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='imovel',
            name='iptu',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]