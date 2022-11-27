from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
# Create your models here.

User = get_user_model()


class Smack(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Smack : {self.title} By:  {self.author}"
