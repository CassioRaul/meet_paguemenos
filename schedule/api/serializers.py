from rest_framework import serializers
from schedule import models

class ScheduleSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Schedule
        fields = ('__all__' ) # ('campo', 'campo')

class ScheduleDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.DelSchedule
        fields = ('__all__')
