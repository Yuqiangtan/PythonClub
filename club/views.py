from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse_lazy
from .forms import MeetingForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def resources(request):
    resource_list=Resource.objects.all()
    return render(request,'club/resources.html',{'resource_list':resource_list})

def meeting(request):
    meeting_list=Meeting.objects.all()
    return render(request,'club/meeting.html',{'meeting_list':meeting_list})

def meetingDetail(request,id):
    meeting=get_object_or_404(Meeting, pk=id)
    return render(request,'club/meetingdetail.html',{'meeting':meeting})

@login_required
def newMeeting(request):
    form=MeetingForm

    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request,'club/newmeeting.html',{'form':form})

def loginmessage(request):
    return render(request,'club/loginmessage.html')

def logoutmessage(request):
    return render(request,'club/logoutmessage.html')