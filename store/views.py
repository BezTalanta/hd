from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .models import Store


class StoreDetailView(View):

    def get(self, request, id):
        if Store.objects.exists(pk=id):
            return render(Store.objects.get(pk=id))
        return redirect(reverse('home'))
