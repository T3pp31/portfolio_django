from django.contrib import admin
from import_export.admin import ImportMixin
from import_export.fields import Field
from import_export.formats import base_formats
from import_export.resources import ModelResource

from .models import *


# Register your models here.
class FinancialInfoResource(ModelResource):
    stock_id = Field(attribute="stock_id", column_name="symbol")
    date = Field(attribute="date", column_name="asOfDate")
    total_revenue = Field(
        attribute="total_revenue", column_name="TotalRevenue"
    )
    stockholdersequity = Field(
        attribute="stockholdersequity", column_name="StockholdersEquity"
    )
    totalassets = Field(attribute="totalassets", column_name="TotalAssets")
    capitaladequancyratio = Field(
        attribute="capitaladequancyratio", column_name="capitalAdequacyRatio"
    )
    roe = Field(attribute="roe", column_name="ROE")

    class Meta:
        model = FinancialInfo

        import_order = (
            "stock_id",
            "date",
            "total_revenue",
            "stockholdersequity",
            "totalassets",
            "capitaladequancyratio",
            "roe",
        )
        import_id_fields = ["stock_id"]


class FinancialInfoAdmin(ImportMixin, admin.ModelAdmin):
    list_display = (
        "stock_id",
        "date",
        "total_revenue",
        "stockholdersequity",
        "totalassets",
        "capitaladequancyratio",
        "roe",
    )
    resource_class = FinancialInfoResource
    formats = [base_formats.CSV]


class MetricsResource(ModelResource):
    stock_id = Field(attribute="stock_id", column_name="ticker")
    stock_name = Field(attribute="stock_name", column_name="ticker_name")
    market = Field(attribute="market", column_name="market_product_category")
    stock_category33 = Field(
        attribute="stock_category33", column_name="type_33"
    )
    stock_category17 = Field(
        attribute="stock_category17", column_name="type_17"
    )
    dividendRate = Field(attribute="dividendRate", column_name="dividendRate")
    dividendYield = Field(
        attribute="dividendYield", column_name="dividendYield"
    )
    fiveYearAvgDividendYield = Field(
        attribute="fiveYearAvgDividendYield",
        column_name="fiveYearAvgDividendYield",
    )
    payoutRatio = Field(attribute="payoutRatio", column_name="payoutRatio")
    marketcap = Field(attribute="marketcap", column_name="MarketCap")
    totalRevenue = Field(attribute="totalRevenue", column_name="totalRevenue")
    roe = Field(attribute="roe", column_name="ROE")

    class Meta:
        model = Metrics

        import_order = (
            "stock_id",
            "stock_name",
            "market",
            "stock_category33",
            "stock_category17",
            "dividendRate",
            "dividendYield",
            "fiveYearAvgDividendYield",
            "payoutRatio",
            "marketcap",
            "totalRevenue",
            "roe",
        )
        import_id_fields = ["stock_id"]


class MetricsAdmin(ImportMixin, admin.ModelAdmin):
    list_display = (
        "stock_id",
        "stock_name",
        "market",
        "stock_category33",
        "stock_category17",
    )
    resource_class = MetricsResource
    formats = [base_formats.CSV]


admin.site.register(FinancialInfo, FinancialInfoAdmin)
admin.site.register(Metrics, MetricsAdmin)
