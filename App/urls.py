from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('PricePage/', views.PricePage, name='PricePage'),
    path('hidden/', views.hidden, name='hidden'),
    
]