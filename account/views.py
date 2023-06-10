from datetime import datetime, timedelta
from random import randint
from uuid import uuid4

import ghasedakpack
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, reverse
from django.views import View

from .forms import LoginForm, RegisterOtpForm, CheckOtpForm
from .models import Otp, User

SMS = ghasedakpack.Ghasedak("1065b3cd468d2a911a79ad4b20400ab95163389aef5a5fc1d0eda477d255d003")


class UserLogin(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('home:home'))
        return super().dispatch(request, *args, **kwargs)

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
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('home:home'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = RegisterOtpForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = RegisterOtpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            randcode = randint(1000, 9999)
            SMS.verification({'receptor': cd["phone"], 'type': '1', 'template': 'solishop', 'param1': randcode})
            token = str(uuid4())
            Otp.objects.create(phone=cd['phone'], code=randcode, token=token,
                               expiration_date=datetime.now() + timedelta(minutes=2))
            request.session['user_registration_info'] = {
                'phone': cd['phone'],
                'password': cd['password']
            }
            print(randcode)
            return redirect(reverse('account:check_otp') + f'?token={token}')
        else:
            form.add_error("phone", "form isn't valid")

        return render(request, 'account/register.html', {'form': form})


class CheckOtpView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('home:home'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        try:
            user_session = request.session['user_registration_info']
            phone = user_session['phone']
            form = CheckOtpForm()
            return render(request, 'account/check_otp.html', {'form': form, 'phone': phone})
        except:
            return redirect('home:home')

    def post(self, request):
        token = request.GET.get('token')
        form = CheckOtpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            check_otp = Otp.objects.filter(code=cd['code'], token=token, expiration_date__gt=datetime.now())
            if check_otp.exists():
                user_session = request.session['user_registration_info']
                new_user = User(
                    phone=user_session['phone'],
                )
                new_user.set_password(user_session['password'])
                new_user.save()
                check_otp.delete()
                # otp = Otp.objects.get(token=token)
                # user = User.objects.create_user(phone=otp.phone)
                del user_session
                login(request, new_user)
                return redirect('/')
            else:
                form.add_error("code", "Code isn't valid")
        else:
            form.add_error("code", "form isn't valid")

        return render(request, 'account/check_otp.html', {'form': form})
