from django.urls import path
from . import views  # Importa as views do aplicativo

urlpatterns = [
    path('', views.index, name='index'), 
    path('servicos/', views.servicos, name='servicos'),
    path('equipe/', views.equipe, name='equipe'), 
    path('contato/', views.contato, name='contato'),  
    path('antesDepois/', views.antesDepois, name='antesDepois'),  
]
