# Generated by Django 4.2.3 on 2023-07-11 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good_stock', '0002_alter_financialinfo_options_alter_metrics_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialinfo',
            name='capitaladequancyratio',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='financialinfo',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='financialinfo',
            name='roe',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='financialinfo',
            name='stock_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='financialinfo',
            name='stockholdersequity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='financialinfo',
            name='total_revenue',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='financialinfo',
            name='totalassets',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='dividendRate',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='dividendYield',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='fiveYearAvgDividendYield',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='market',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='marketcap',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='payoutRatio',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='roe',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='stock_category17',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='stock_category33',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='stock_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='stock_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='metrics',
            name='totalRevenue',
            field=models.IntegerField(null=True),
        ),
    ]
