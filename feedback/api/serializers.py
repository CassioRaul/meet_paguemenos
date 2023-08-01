from rest_framework import serializers
from feedback import models

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feedback
        fields = '__all__' #campo
