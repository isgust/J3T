from django.urls import path
from . import views  # Importa as views do aplicativo

urlpatterns = [
    path('', views.index, name='index'), 
    path('contato/', views.contato, name='contato'),  
    path('quemSomos/', views.quemSomos, name='quemSomos'), 
    path('servicos/', views.servicos, name='servicos'),  
]
