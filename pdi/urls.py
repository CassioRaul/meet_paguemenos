from . import views
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pdi.api import viewsets as pdiviewsets
from pdi.api import viewsets as planningdeleteviewset

route = routers.DefaultRouter()
route.register(r'', pdiviewsets.PlanningViewSet)
route.register(r'', planningdeleteviewset.PlanningDeleteViewSet)
urlpatterns = [
    path('pdi/', include(route.urls)),
    path('delete&planning/', include(route.urls)),
]
