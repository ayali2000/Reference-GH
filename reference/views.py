from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import *

# Create your views here.

def index(request):
    return render(request,'reference/index.html')


def reference_view(request):
    stations = ReferenceStation.objects.all()
    context ={
        'stations':stations
    }
    return render(request,'reference/ref.html', context)

@login_required()
def chat_view(request):
    chat = Chat.objects.all()
    context = {
        'chat':chat
    }
    return render(request,'reference/chatpage.html',context)