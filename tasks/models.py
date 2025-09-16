from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=50)
    description = models.TextField(default="")
    complated = models.BooleanField(default=False)
    created_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


