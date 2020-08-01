from enum import Enum
from django.db import models
from django.http import HttpResponse
from rest_enumfield import EnumField


class BirdColors(Enum):
    BLACK = 'black'
    WHITE = 'white'
    BLACK_WHITE = 'black & white'
    GREY = 'grey'
    RED = 'red'
    RED_WHITE = 'red & white'


class Bird(models.Model):
    name = models.TextField()
    color = EnumField(choices=BirdColors)
    body_length = models.IntegerField()
    wingspan = models.IntegerField()


def version(request):
    return HttpResponse('Birds Service. Version 0.1')