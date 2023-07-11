from django.db import models


# Create your models here.
class Metrics(models.Model):
    stock_id = models.CharField(max_length=100)
    stock_name = models.CharField(max_length=100)
    market = models.CharField(max_length=100)
    stock_category33 = models.CharField(max_length=100)
    stock_category17 = models.CharField(max_length=100)

    dividendRate = models.IntegerField()

    dividendYield = models.IntegerField()

    fiveYearAvgDividendYield = models.IntegerField()

    payoutRatio = models.IntegerField()

    marketcap = models.IntegerField()

    totalRevenue = models.IntegerField()

    roe = models.IntegerField()

    class Meta:
        verbose_name = "Metrics"


class FinancialInfo(models.Model):
    stock_id = models.CharField(max_length=100)
    date = models.DateTimeField()
    total_revenue = models.IntegerField()
    stockholdersequity = models.IntegerField()
    totalassets = models.IntegerField()
    capitaladequancyratio = models.IntegerField()
    roe = models.IntegerField()

    class Meta:
        verbose_name = "FinancialInfo"
