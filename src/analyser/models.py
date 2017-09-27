from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField


class Packages(models.Model):
    os = models.TextField()
    resource = models.TextField()
    provider = models.TextField()
    title = models.TextField()
    version = ArrayField(models.TextField())

    def __str__(self):
        return '%s: %s' % (self.os, self.title)

class Users(models.Model):
    os = models.TextField()
    resource = models.TextField()
    shell = models.TextField()
    title = models.TextField()
    uid = models.IntegerField()
    comment = models.TextField()
    home = models.TextField()
    gid = models.IntegerField()
    groups = ArrayField(models.TextField(), blank=True)

    def __str__(self):
        return '%s: %s' % (self.os, self.title)

class Volumes(models.Model):
    os = models.TextField()
    volume_name = models.TextField()
    available = models.TextField()
    available_bytes = models.BigIntegerField()
    used = models.TextField()
    capacity = models.TextField()
    size = models.TextField()
    options = ArrayField(models.TextField(), blank=True)
    size_bytes = models.BigIntegerField()
    used_bytes = models.BigIntegerField()
    device = models.TextField()
    filesystem = models.TextField()

    def __str__(self):
        return '%s: %s' % (self.os, self.volume_name)
