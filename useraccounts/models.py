from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.

class UserProfle(models.Model):
    user = models.OneToOneField(User, unique=True)
    address = models.CharField(max_length=255,blank=True,default="")

    def __unicode__(self):
        return str(self.user)

class Todos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=False,null=False)
    description = models.CharField(max_length=255,blank=True,default="")
    done_by = models.CharField(max_length=100,blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('todo-detail', kwargs={'pk': self.pk})
