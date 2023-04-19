from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField()
    age = models.IntegerField()
    sex = models.CharField(max_length=1, null=True)
    create = models.DateTimeField()
