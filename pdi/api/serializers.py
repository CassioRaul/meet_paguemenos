from rest_framework import serializers
from pdi import models

class PlanningSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Planning
        fields = '__all__' # ['campo']
    
class PlanningDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.DelPlanning
        fields = '__all__'