from enum import Enum
from django.db import models
from django.http import HttpResponse
from enumchoicefield import EnumChoiceField, ChoiceEnum
from enumchoicefield.enum import PrettyEnum
from rest_enumfield import EnumField


class Bird(models.Model):
    class Meta:
        db_table = u'birds'

    name = models.TextField(primary_key=True)
    color = models.TextField()
    species = models.TextField()
    body_length = models.IntegerField()
    wingspan = models.IntegerField()


def version(request):
    return HttpResponse('Birds Service. Version 0.1')
