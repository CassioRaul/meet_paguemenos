from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers
from home.api import viewsets as homeviewsets

route = routers.DefaultRouter()
route.register(r'Gerente', homeviewsets.ManagerViewSet)
route.register(r'Colaborador', homeviewsets.CollaboratorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    # path('home/', views.home, name="home"),
    # path('editar_user_manag/<int:id>', views.editar_user_manag, name="editar_user_manag"),
    # path('editar_user_collab/<int:id>', views.editar_user_collab, name="editar_user_collab"),
    # path('update_user_manag/<int:id>', views.update_user_manag, name="update_user_manag"),
    # path('update_user_collab/<int:id>', views.update_user_collab, name="update_user_collab"),
    # path('delete_user_manag/<int:id>', views.delete_user_manag, name="delete_user_manag"),
    # path('delete_user_collab/<int:id>', views.delete_user_collab, name="delete_user_collab"),
    # path('cadastro/', views.cadastro, name="cadastro"),
    # path('login/', views.login, name="login"),
]
