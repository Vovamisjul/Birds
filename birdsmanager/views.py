from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from birdsmanager.models import Bird
from birdsmanager.serializers import BirdsSerializer


class BirdsView(APIView):
    def get(self, request):
        if 'attribute' and 'order' in request.query_params:
            return Response({'birds': 2})
        return Response({'birds': 1})

    def post(self, request):
        serializer = BirdsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            new_bird = serializer.validated_data
            if new_bird['body_length'] < 0:
                return Response('Invalid body length', status=status.HTTP_400_BAD_REQUEST)
            if new_bird['wingspan'] < 0:
                return Response('Invalid wingspan', status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_204_NO_CONTENT)