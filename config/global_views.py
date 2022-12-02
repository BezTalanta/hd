from django.shortcuts import render, redirect
from django.views import View
import environ
environ.Env.read_env('psql.env')


class Test(View):


    def get(self, request):
        print(environ.Env()('DB_NAME'))
        print(environ.Env()('DB_USER'))
        print(environ.Env()('DB_PASSWORD'))
        print(environ.Env()('SECRET_KEY'))
        return redirect('/')


class DashboardView(View):

    def get(self, request):
        return render(request, 'dashboard.html')
