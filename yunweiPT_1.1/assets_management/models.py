from __future__ import unicode_literals

from django.db import models

class MachineRoom(models.Model):
    macroom = models.CharField(max_length=100)
    def __unicode__(self):
        return self.macroom

class Cabinet(models.Model):
    cabinet = models.CharField(max_length=100)
    room = models.ForeignKey(MachineRoom)
    def __unicode__(self):
        return self.cabinet

class Machines(models.Model):
#    trademark = models.CharField(max_length=100)
    ip = models.GenericIPAddressField(max_length=100)
    role = models.CharField(max_length=50)
    hardwareinfo = models.CharField(max_length=200)
    gameinfo = models.CharField(max_length=300)
    cb = models.ForeignKey(Cabinet,blank=True, null=True)
    room = models.ForeignKey(MachineRoom,blank=True, null=True)
    def __unicode__(self):
        return self.ip