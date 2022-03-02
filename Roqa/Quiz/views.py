
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreatingQuizForm, QuestionViewForm
from .models import Quiz, Questions, Options, CorrectOptions, TestLogs, UsersGivingTest, RecordedResponses,User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from random import shuffle
from django.db.models import Q
from django.utils import timezone
import xlwt
import json
import base64
from django.core.files.base import ContentFile
from django.db.models import Avg
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout

def LoginView(request):
    if request.method=="POST":
        if request.user.is_authenticate:
            re
    return render(request, 'login.html')




def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
 
 
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'main/index.html')