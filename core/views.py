# core/views.py
from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# ... la tua view homepage ...
def homepage(request):
    return render(request, 'homepage.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')