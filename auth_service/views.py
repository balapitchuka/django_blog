from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            return HttpResponse("received form")
        else:
            return HttpResponse('invalid form')
    else:
        form = UserCreationForm()
        return render(request, 'auth_service/register.html', {'form' : form} )
        
