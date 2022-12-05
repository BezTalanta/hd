from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .models import Store
from .forms import StoreForm


class StoreDetailView(View):

    def get(self, request, id):
        if Store.objects.exists(pk=id):
            return render(Store.objects.get(pk=id))
        return redirect(reverse('home'))


class StoreSelect(View):

    def get(self, request):
        return render(request, 'store/select_store.html', {
            'form': StoreForm(instance=request.user),
        })

    def post(self, request):
        sf = StoreForm(request.POST, instance=request.user)
        if sf.is_valid():
            sf.save()
        return redirect(reverse('store'))
