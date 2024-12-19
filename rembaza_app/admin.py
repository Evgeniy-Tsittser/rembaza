from django.contrib import admin
from .models import WaterTable, MonthWorks, SeverageTable

@admin.register(MonthWorks)
class MonthWorksAdmin(admin.ModelAdmin):
    list_display = ('year', 'month', 'completed_works', 'description', 'volume', 'summ')
    list_filter = ('type_work', 'year', 'month')
    search_fields = ['completed_works']


@admin.register(WaterTable)
class WaterTableAdmin(admin.ModelAdmin):
    list_display = ('year', 'completed_works', 'year_total')
    search_fields = ['completed_works']


@admin.register(SeverageTable)
class SeverageTableAdmin(admin.ModelAdmin):
    list_display = ('year', 'completed_works', 'year_total')
    search_fields = ['completed_works']


