from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.conf import settings

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=50)
    description = models.TextField(default="")
    complated = models.BooleanField(default=False)
    created_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def CreateToken(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
    