from django.db import models

class UserInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    
    
class Questionnaire(models.Model):
    # Ajoutez les champs de votre questionnaire ici
    question_1 = models.CharField(max_length=255)
    question_2 = models.CharField(max_length=255)
    # Ajoutez autant de champs que nécessaire pour votre questionnaire    
