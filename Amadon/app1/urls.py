from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path("buy",views.buy),
    path("pay", views.pay)
]
