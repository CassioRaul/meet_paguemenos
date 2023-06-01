from . import views
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from schedule.api import viewsets as scheduleviewsets
from schedule.api import viewsets as scheduleseleteserializerssiewset

route = routers.DefaultRouter()
route.register(r'', scheduleviewsets.ScheduleViewSet)
route.register(r'', scheduleseleteserializerssiewset.ScheduleDeleteSerializersViewSet)

urlpatterns = [
    path('schedule/', include(route.urls)),
    path('delete_schedule/', include(route.urls)),
]
