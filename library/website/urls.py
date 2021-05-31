from django.urls import path
from . import views
from users import views as view_contact


urlpatterns = [
    path('', views.home, name='website-home'),
    path('about/', views.about, name='website-about'),
    path('catalog/', views.catalog, name='website-catalog'),
    path('contact/', view_contact.contactView, name='users-contact')
]