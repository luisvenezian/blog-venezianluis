from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # Início
    path('', views.home_page),
    path('cv/', views.cv),
    path('assinatura/', views.assinatura, name = 'assinatura'),
    path('menu/<str:assunto>', views.home_page, name = 'menu')
]
