from django.urls import path
from .views import StoreDetailView, StoreSelect

urlpatterns = [
    path('store_select/', StoreSelect.as_view(), name='store_select'),
    path('detail/<int:id>/', StoreDetailView.as_view(), name='store_detail')
]
