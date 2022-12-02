from django.urls import path
from .views import StoreDetailView

urlpatterns = [
    path('detail/<int:id>/', StoreDetailView.as_view(), name='store_detail')
]
