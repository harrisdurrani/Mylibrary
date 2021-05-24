from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='website-home'),
    path('about/', views.about, name='website-about'),
    path('catalog/', views.catalog, name='website-catalog'),
]