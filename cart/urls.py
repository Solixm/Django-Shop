from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('detail', views.CartDetailView.as_view(), name='detail')
]
