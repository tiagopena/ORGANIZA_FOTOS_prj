from django.urls import path
from criar_lista_app import views


urlpatterns = [
    path('', views.menu, name='menu'),

]