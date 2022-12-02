from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView

from .views import (
    LSignupView,
    LoginView,
)

urlpatterns = [
    # path('',
    #      TemplateView.as_view(template_name='account/home_page.html'),
    #      name='home'),
    path('signup/', LSignupView.as_view(), name='signup'),
    path('logout/',
         LogoutView.as_view(next_page=reverse_lazy('store')),
         name='logout'),
    path('login/', LoginView.as_view(), name='login'),
]
