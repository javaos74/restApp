# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.

class Domain(models.Model):
    name = models.CharField(max_length=64)
    controllers = models.CharField(max_length=64)
    user = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    created_date = models.DateTimeField(default=timezone.now)


class EPTracker(models.Model):
    mac = models.CharField(max_length=18)
    ip = models.CharField(max_length=16)
    domain = models.CharField(max_length=64)
    tenant = models.CharField(max_length=100)
    app = models.CharField(max_length=100)
    epg = models.CharField(max_length=100)
    dn = models.CharField(max_length=2048)
    intf = models.CharField(max_length=2048)
    start = models.CharField(max_length=24)
    stop = models.CharField(max_length=24)


class FaultMessage(models.Model):
    code = models.CharField(max_length=8)
    title = models.CharField(max_length=512)
    syslog = models.TextField()
    explan = models.TextField()
    actions = models.TextField()
