# Generated by Django 4.2.3 on 2023-07-11 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('good_stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='financialinfo',
            options={'verbose_name': 'FinancialInfo'},
        ),
        migrations.AlterModelOptions(
            name='metrics',
            options={'verbose_name': 'Metrics'},
        ),
    ]
