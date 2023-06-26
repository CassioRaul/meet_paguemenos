from django.shortcuts import render
from .models import Feedback #, DeleteFeedbackG,FeedbackC, DeleteFeedbackC

def feedback(request):
    feedback = Feedback.objects.all()
    # delete_feedbackG = DeleteFeedbackG.objects.all()
    # feedbackC = FeedbackC.objects.all()
    # delete_feedbackC = DeleteFeedbackC.objects.all()

    context={
        'feedbacks': feedback,
        # 'delete_feedbacksg': delete_feedbackG,
        # 'feedbacksc': feedbackC,
        # 'delete_feedbacksc': delete_feedbackC,
    }
    return render(request, "index.html", context)
