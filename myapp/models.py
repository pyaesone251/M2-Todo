from django.db import models

# Create your models here.

class TodoappModel(models.Model):
    task = models.CharField(max_length=200)
    note = models.TextField()
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)