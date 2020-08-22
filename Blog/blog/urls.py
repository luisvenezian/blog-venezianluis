from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # Início
    path('', views.home_page),
    path('cv/', views.cv),
    path('assinatura/', views.assinatura, name = 'assinatura'),
    path('menu/<str:assunto>', views.home_page, name = 'menu'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('escrever/', views.escrever, name = 'escrever'),
    path('gostar/', views.gostar, name = 'gostar'),
    path('comentarios/', views.comentarios, name = 'comentarios'),
    path('comentar/', views.comentar, name = 'comentar'),
]   
