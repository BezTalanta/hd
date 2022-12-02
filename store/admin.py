from django.contrib import admin

from .views import Store


class StoreAdmin(admin.ModelAdmin):
    list_display = ['city', 'full_address']
    list_filter = ['city']


admin.site.register(Store, StoreAdmin)
