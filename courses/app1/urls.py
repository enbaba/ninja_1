from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('app1/create', views.create),
    path('app1/<int:id>', views.comments),
    path('app1/<int:id>/comment', views.create_comment),
    path('app1/<int:id>/delete', views.delete)
]