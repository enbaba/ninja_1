from django.urls import path
from . import views

urlpatterns = [
    path('', views.randomw),
    # path('random_word', views.random_word),
    path('reset', views.reset)

]