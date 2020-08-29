from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('app1/new', views.new),
    path('app1/create', views.create),
    path('app1/<int:show_id>/update', views.update),
    path('app1/<int:show_id>', views.show),
    path('app1/<int:show_id>/delete', views.delete)
# app/5
]

