from django.contrib import admin

from .models import Store, History


class StoreAdmin(admin.ModelAdmin):
    list_display = ['city', 'full_address']
    list_filter = ['city']


class HistoryAdmin(admin.ModelAdmin):
    readonly_fields = ['date']

admin.site.register(Store, StoreAdmin)
admin.site.register(History, HistoryAdmin)
