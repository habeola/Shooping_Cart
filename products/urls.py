from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index_url'),
    path('new/', views.new, name='name_url')
]