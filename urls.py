from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Vue pour afficher le formulaire d'informations utilisateur
    path('questionnaire/', views.fill_questionnaire, name='fill_questionnaire'),  # Vue pour afficher le formulaire de questionnaire
    path('merci/', views.thank_you, name='thank_you'),  # Vue pour afficher la page de remerciement
]
