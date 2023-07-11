from django.db import models


# Create your models here.
class Metrics(models.Model):
    stock_id = models.CharField(max_length=100, null=True, blank=True)
    stock_name = models.CharField(max_length=100, null=True, blank=True)
    market = models.CharField(max_length=100, null=True, blank=True)
    stock_category33 = models.CharField(max_length=100, null=True, blank=True)
    stock_category17 = models.CharField(max_length=100, null=True, blank=True)
    dividendRate = models.CharField(max_length=100, null=True, blank=True)
    dividendYield = models.CharField(max_length=100, null=True, blank=True)
    fiveYearAvgDividendYield = models.CharField(
        max_length=100, null=True, blank=True
    )
    payoutRatio = models.CharField(max_length=100, null=True, blank=True)
    marketcap = models.CharField(max_length=100, null=True, blank=True)
    totalRevenue = models.CharField(max_length=100, null=True, blank=True)
    roe = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Metrics"

    def __str__(self):
        return self.stock_id


class FinancialInfo(models.Model):
    stock_id = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    total_revenue = models.CharField(max_length=100, null=True, blank=True)
    stockholdersequity = models.CharField(
        max_length=100, null=True, blank=True
    )
    totalassets = models.CharField(max_length=100, null=True, blank=True)
    capitaladequancyratio = models.CharField(
        max_length=100, null=True, blank=True
    )
    roe = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "FinancialInfo"

    def __str__(self):
        return self.stock_id