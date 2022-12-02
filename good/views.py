from django.shortcuts import render, redirect
from django.views import View
from django.core.paginator import Paginator
from django.urls import reverse
from django.conf import settings

from .models import Good
from .forms import GoodForm
import config.cute_logging as clog


class HomeView(View):

    def get(self, request):
        pages = Paginator(Good.objects.all().using(
            settings.SLAVE_NAME), 10)
        get_page = request.GET.get('page', False) or \
            request.session.get('page', False)
        if get_page is False or (get_page is not False and int(get_page) < 1):
            get_page = 1
        elif int(get_page) > pages.num_pages:
            get_page = pages.num_pages

        pages = pages.page(int(get_page))
        clog.message(f'\t{pages.object_list}', clog.GOOD)
        return render(request, 'good/home.html', {
            'goods_part_1': pages.object_list[0:5],
            'goods_part_2': pages.object_list[5:10],
            'page': pages,
        })

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect(reverse('login'))
        object_to_buy = Good.objects.using(settings.SLAVE_NAME).get(
            artikul=request.POST['buy_artikul'])
        object_to_buy.buy_amount += 1
        object_to_buy.save()
        request.session['artikul_bought'] = object_to_buy.artikul
        request.session['page'] = request.POST['page']
        return redirect(reverse('store'))


class DetailView(View):

    def get(self, request, id):
        clog.message(f'\tidx: {id}', clog.GOOD)
        return render(request, 'good/detail.html', {
            'form': GoodForm(instance=Good.objects.get(pk=id)),
        })
