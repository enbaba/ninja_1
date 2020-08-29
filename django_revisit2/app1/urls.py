from django.urls import path
from .import views

urlpatterns = [
    # loads main page
    path('', views.index),
    # loads the results page 
    path('result',views.result),
    
    # when you push submit it does this 
    path('process',views.process)
]
