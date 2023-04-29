# from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect



# Create your views here.

# from django.forms import modelform_factory 

from .models import Meeting,Room
from .form  import MeetingForm


def detail(request,id):
    # meeting=Meeting.objects.get(pk=id)
    meeting=get_object_or_404(Meeting,pk=id)


    return render(request,'meeting/detail.html',{"meeting":meeting})

def rooms_list(request):
    return render (request,'meeting/room_list.html',{'rooms':Room.objects.all()})

## MeetingForm=modelform_factory(Meeting,exclude=[])

def form(request):
    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form=MeetingForm()
    
    
    return render(request,'meeting/form.html',{'form':form})