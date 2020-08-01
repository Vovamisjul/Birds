from rest_enumfield import EnumField
from rest_framework import serializers

from birdsmanager.models import BirdColors


class BirdsSerializer(serializers.Serializer):
    name = serializers.CharField()
    color = EnumField(choices=BirdColors)
    body_length = serializers.IntegerField()
    wingspan = serializers.IntegerField()