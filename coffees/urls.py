from django.urls import path

from . import views

urlpatterns = [
    # ex: /coffees/
    path('', views.index),
]

from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('coffees:index'), name='root'),
    ...
]


from django.urls import path

from . import views

app_name = 'coffees'
urlpatterns = [
    # ex: /coffees/
    path('', views.index, name='index'),
]