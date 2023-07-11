from django.contrib import admin
from import_export.admin import ImportExportMixin, ImportMixin
from import_export.formats import base_formats
from import_export.resources import ModelResource

from .models import *


# Register your models here.
class FinancialInfoResource(ModelResource):
    class Meta:
        model = FinancialInfo


class MetricsResource(ModelResource):
    class Meta:
        model = Metrics


class FinancialInfoResourceAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = FinancialInfoResource


class MetricsResourceAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = MetricsResource


admin.site.register(FinancialInfo)
admin.site.register(Metrics)
