from django.urls import path
from criar_lista_app import views

app_name = 'criar_lista_app'

urlpatterns = [
    path('', views.menu, name='menu'),
    path('gerar_lista/', views.gerar_lista, name='gerar_lista'),
    path('comparar_lista/', views.comparar_lista, name='comparar_lista'),
    path('mostrar_resultado/', views.mostrar_resultado, name='mostrar_resultado'),    
]