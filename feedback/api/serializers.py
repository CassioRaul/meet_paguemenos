from rest_framework import serializers
from feedback import models

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feedback
        fields = '__all__' #campo

# class DeleteFeedbackGSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.DeleteFeedbackG
#         fields = '__all__' #campo


# class FeedbackCSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.FeedbackC
#         fields = '__all__' #campo

# class DeleteFeedbackCSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.DeleteFeedbackC
#         fields = '__all__' #campo