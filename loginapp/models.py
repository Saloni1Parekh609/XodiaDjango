from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)
    gameswon=models.IntegerField(default=0)
    gameslost=models.IntegerField(default=0)
    gamesdrawn=models.IntegerField(default=0)
    points=models.IntegerField(default=0)
    college = models.TextField(max_length=500, default='')
    mobile=models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)

    #botpath = models.CharField(max_length=30)
    #botextension = models.TextField(max_length=500)
    """def __str__(self):
        return self.user"""

    def __str__(self):
        return self.user.name
