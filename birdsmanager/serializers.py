from enumchoicefield import EnumChoiceField
from rest_enumfield import EnumField
from rest_framework import serializers

from birdsmanager.models import  Bird


class BirdsSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = u'birds'
        model = Bird
        fields = '__all__'
    name = serializers.CharField()
    color = serializers.CharField()
    species = serializers.CharField()
    body_length = serializers.IntegerField()
    wingspan = serializers.IntegerField()

    def create(self, validated_data):
        return Bird.objects.create(**validated_data)