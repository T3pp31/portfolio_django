# Generated by Django 4.2.3 on 2023-07-11 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good_stock', '0007_alter_metrics_dividendrate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialinfo',
            name='capitaladequancyratio',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='financialinfo',
            name='roe',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='financialinfo',
            name='stockholdersequity',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='financialinfo',
            name='total_revenue',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='financialinfo',
            name='totalassets',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='dividendRate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='dividendYield',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='fiveYearAvgDividendYield',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='marketcap',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='payoutRatio',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='roe',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='totalRevenue',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
