from django.urls import path
from .views import Index, Search, About

urlpatterns = [
    path('', Index, name = 'home'),
    path('q', Search, name='generate'),
    path('about', About, name='about')
]
