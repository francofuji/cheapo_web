from __future__ import unicode_literals

from django.db import models


class Unit(models.Model):
    name = models.CharField(max_length=10)
    code = models.CharField(max_field=3)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    unit = models.ForeignKey(Unit)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name