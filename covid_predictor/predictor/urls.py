from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict_covid, name='predict'),
    path('dashboard/', views.dash, name='dash'),
    path('account/', views.acc, name='acc'),
    #path('medical-history/', views.medical, name='medical'),
    path('log/', views.logout_view, name='log'),
]