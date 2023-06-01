from . import views
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pdi.api import viewsets as pdiviewsets
from pdi.api import viewsets as planningdeleteviewset

route_pdi = routers.DefaultRouter()
route_pdi.register(r'', pdiviewsets.PlanningViewSet)

route_delete_pdi = routers.DefaultRouter()
route_delete_pdi.register(r'', planningdeleteviewset.PlanningDeleteViewSet)

urlpatterns = [
    path('pdi/', include(route_pdi.urls)),
    path('delete_pdi/', include(route_delete_pdi.urls)),
]
