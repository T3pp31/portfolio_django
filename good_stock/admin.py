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


@admin.register(FinancialInfo)
class FinancialInfoResourceAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = FinancialInfoResource


@admin.register(Metrics)
class MetricsResourceAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = MetricsResource


admin.site.register(FinancialInfo)
admin.site.register(Metrics)
admin.site.register(FinancialInfoResourceAdmin)
admin.site.register(MetricsResourceAdmin)
