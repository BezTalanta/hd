from django.contrib import admin

from .models import Good


class GoodAdmin(admin.ModelAdmin):
    list_display = ['artikul', 'title', 'price', 'buy_amount']
    list_filter = ['artikul', 'price', 'title', 'buy_amount']
    list_editable = ['title', 'price', 'buy_amount']
    readonly_fields = ['artikul']


admin.site.register(Good, GoodAdmin)
