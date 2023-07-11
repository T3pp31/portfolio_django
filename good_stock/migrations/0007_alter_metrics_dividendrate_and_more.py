# Generated by Django 4.2.3 on 2023-07-11 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good_stock', '0006_alter_metrics_dividendrate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metrics',
            name='dividendRate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='dividendYield',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='fiveYearAvgDividendYield',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='marketcap',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='payoutRatio',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='roe',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='totalRevenue',
            field=models.FloatField(blank=True, null=True),
        ),
    ]