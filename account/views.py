from random import randint
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from .forms import LoginForm, RegisterOtpForm, CheckOtpForm
from django.contrib.auth import authenticate, login

from .models import Otp, User




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
            Otp.objects.create(phone=cd['phone'], code=randcode)
            print(randcode)
            return redirect(reverse_lazy('account:check_otp') + f'?phone={cd["phone"]}')

        return render(request, 'account/register.html', {'form': form})


class CheckOtpView(View):
    def get(self, request):
        form = CheckOtpForm()
        return render(request, 'account/check_otp.html', {'form': form})

    def post(self, request):
        phone = request.GET.get('phone')
        form = CheckOtpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if Otp.objects.filter(code=cd['code'], phone=phone).exists():
                user = User.objects.create_user(phone=phone)
                login(request, user)
                return redirect('/')

        return render(request, 'account/check_otp.html', {'form': form})
