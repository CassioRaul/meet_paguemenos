from django.shortcuts import render
from .models import Feedback, DeleteFeedback

def feedback(request):
    feedback = Feedback.objects.all()
    delete_feedback = DeleteFeedback.objects.all()
    context={
        'feedbacks': feedback,
        'delete_feedbacks': delete_feedback,
    }
    return render(request,"index.html",context)
