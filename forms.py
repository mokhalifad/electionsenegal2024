from django import forms
from .models import UserInfo, Questionnaire

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['first_name', 'last_name', 'email']

class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = ['question_1', 'question_2']  # Ajoutez tous les champs du questionnaire

