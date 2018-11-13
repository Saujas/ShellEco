from django.shortcuts import render, render_to_response
from .models import Detail
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf


def index(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']

        obj = Detail(name=name, email=email, number=number)
        obj.save()
   
    
    return render(request, 'pages/teamBits.html')


def team(request):
    return render(request, 'pages/teamBitsTeam.html')


def efficiency(request):
    return render(request, 'pages/teamBitsEfficiency.html')










