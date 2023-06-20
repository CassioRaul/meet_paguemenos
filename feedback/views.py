from django.shortcuts import render
from .models import FeedbackG, DeleteFeedbackG,FeedbackC, DeleteFeedbackC

def feedback(request):
    feedbackG = FeedbackG.objects.all()
    delete_feedbackG = DeleteFeedbackG.objects.all()
    feedbackC = FeedbackC.objects.all()
    delete_feedbackC = DeleteFeedbackC.objects.all()


    context={
        'feedbacksg': feedbackG,
        'delete_feedbacksg': delete_feedbackG,
        'feedbacksc': feedbackC,
        'delete_feedbacksc': delete_feedbackC,

    }
    return render(request,"index.html",context)
