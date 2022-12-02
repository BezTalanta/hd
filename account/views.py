from django.contrib.messages import error
from django.contrib.auth import get_user_model, authenticate, login
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View


class HomePage(TemplateView):
    template_name = 'home_page.html'


class LSignupView(View):
    '''
    Low level signup view
    '''

    def get(self, request):
        return render(request, 'account/signup_page.html')

    # TODO: Try to rewrite with form signupview, because of a lot of exceptions
    def post(self, request):
        username = request.POST['username']
        pass1, pass2 = request.POST['pass1'], request.POST['pass2']
        if pass1 != pass2:
            error(request, 'Your passwords are different')
            return render(request, 'account/signup_page.html', {
                'username': username,
            })
        try:
            created_user = get_user_model().objects.create_user(
                email=request.POST['email'],
                username=username,
                password=pass1,
            )
            login(request, created_user)
            return redirect(reverse('store'))
        except Exception as e:
            error(request, str(e))
            return render(request, 'account/signup_page.html', {
                'username': username,
            })


class LoginView(View):
    '''
    Low level login view
    '''

    def get(self, request):
        return render(request, 'account/login_page.html')

    def post(self, request):
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect(reverse('store'))
        error(request, 'Your inputs were incorrect, try again')
        return render(request, 'account/login_page.html', {
            'username': username,
        })
