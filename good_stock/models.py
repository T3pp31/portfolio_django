from django.db import models


# Create your models here.
class Metrics(models.Model):
    stock_id = models.CharField(max_length=100, null=True, blank=True)
    stock_name = models.CharField(max_length=100, null=True, blank=True)
    market = models.CharField(max_length=100, null=True, blank=True)
    stock_category33 = models.CharField(max_length=100, null=True, blank=True)
    stock_category17 = models.CharField(max_length=100, null=True, blank=True)
    dividendRate = models.FloatField(max_length=100, null=True, blank=True)
    dividendYield = models.FloatField(max_length=100, null=True, blank=True)
    fiveYearAvgDividendYield = models.FloatField(
        max_length=100, null=True, blank=True
    )
    payoutRatio = models.FloatField(max_length=100, null=True, blank=True)
    marketcap = models.FloatField(max_length=100, null=True, blank=True)
    totalRevenue = models.FloatField(max_length=100, null=True, blank=True)
    roe = models.FloatField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Metrics"

    def __str__(self):
        return self.stock_id


class FinancialInfo(models.Model):
    stock_id = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    total_revenue = models.FloatField(max_length=100, null=True, blank=True)
    stockholdersequity = models.FloatField(
        max_length=100, null=True, blank=True
    )
    totalassets = models.FloatField(max_length=100, null=True, blank=True)
    capitaladequancyratio = models.FloatField(
        max_length=100, null=True, blank=True
    )
    roe = models.FloatField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "FinancialInfo"

    def __str__(self):
        return self.stock_id


class GoodStock(models.Model):
    stock_id = models.CharField(max_length=100)
    stock_name = models.CharField(max_length=100)
    want_to_buy_dividendYield = models.CharField()
    no_dividend_decrease_year = models.IntegerField(blank=True, null=True)
    dividend_increase_year = models.IntegerField(blank=True, null=True)
