from __future__ import unicode_literals

from django.db import models

# Create your models here.
class userinfo(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    is_active = models.BooleanField()
    privilege = models.CharField(max_length=100)
    def __unicode__(self):
        return self.username
