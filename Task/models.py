from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    usertask = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
