from django.db import models

# Create your models here.
# Create your models here.
class Candidate(models.Model):
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    Confirm_password=models.CharField(max_length=100)
    