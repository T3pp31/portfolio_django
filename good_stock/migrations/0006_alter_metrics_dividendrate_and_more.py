# Generated by Django 4.2.3 on 2023-07-11 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good_stock', '0005_alter_financialinfo_capitaladequancyratio_and_more'),
    ]

    operations = [
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
