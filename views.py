from django.shortcuts import render, redirect
from .forms import UserInfoForm, QuestionnaireForm
from .models import UserInfo


def index1(request):
   context = {"message": "Veiller remplir ce formulaire S.V.P"}
   return render(request, 'election2024\index.html', context)


def index(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fill_questionnaire')
    else:
        form = UserInfoForm()
    return render(request, 'election2024/index.html', {'form': form})

def fill_questionnaire(request):
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = QuestionnaireForm()
    return render(request, 'election2024/questionnaire.html', {'form': form})

def thank_you(request):
    return render(request, 'election2024/merci.html')
