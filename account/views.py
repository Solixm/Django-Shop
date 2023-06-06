from random import randint
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from .forms import LoginForm, RegisterOtpForm, CheckOtpForm
from django.contrib.auth import authenticate, login
# import ghasedak
from .models import Otp, User
from uuid import uuid4


class UserLogin(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(phone=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error("phone", "Form isnt Valid")
        else:
            form.add_error("phone", "Form isnt Valid")

        return render(request, 'account/login.html', {'form': form})


class UserRegister(View):
    def get(self, request):
        form = RegisterOtpForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = RegisterOtpForm(request.POST)
        if form.is_valid():
            randcode = randint(1000, 9999)
            cd = form.cleaned_data
            token = str(uuid4())
            Otp.objects.create(phone=cd['phone'], code=randcode, token=token)
            print(randcode)
            return redirect(reverse_lazy('account:check_otp') + f'?token={token}')

        return render(request, 'account/register.html', {'form': form})


class CheckOtpView(View):
    def get(self, request):
        form = CheckOtpForm()
        return render(request, 'account/check_otp.html', {'form': form})

    def post(self, request):
        token = request.GET.get('token')
        form = CheckOtpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if Otp.objects.filter(code=cd['code'], token=token).exists():
                otp = Otp.objects.get(token=token)
                user = User.objects.create_user(phone=otp.phone)
                login(request, user)
                return redirect('/')

        return render(request, 'account/check_otp.html', {'form': form})
