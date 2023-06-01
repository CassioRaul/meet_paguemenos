from . import views
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from schedule.api import viewsets as scheduleviewsets
from schedule.api import viewsets as scheduleseleteserializerssiewset

route_schedule = routers.DefaultRouter()
route_schedule.register(r'', scheduleviewsets.ScheduleViewSet)

route_delete_schedule = routers.DefaultRouter()
route_delete_schedule.register(r'', scheduleseleteserializerssiewset.ScheduleDeleteSerializersViewSet)

urlpatterns = [
    path('schedule/', include(route_schedule.urls)),
    path('delete_schedule/', include(route_delete_schedule.urls)),
]
