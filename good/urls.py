from django.urls import path
from .views import HomeView, DetailView
from config.global_views import DashboardView


urlpatterns = [
    path('', HomeView.as_view(), name='store'),
    path('dash/', DashboardView.as_view(), name='dash'),
    path('good-detail/<int:id>/', DetailView.as_view(), name='good_detail'),
]
