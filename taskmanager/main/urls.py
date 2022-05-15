from django.urls import path
from . import views
from .views import Search, Home


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),

    path('search/', Search.as_view(), name='search'),

    path('base', Home.as_view(), name='base'),
]
