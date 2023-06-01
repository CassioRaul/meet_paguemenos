from rest_framework import serializers
from home import models

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserManager
        fields = '__all__' # ['campo']

class CollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserManager
        fields = '__all__' # ['campo']

