from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from birdsmanager.models import Bird
from birdsmanager.serializers import BirdsSerializer


class BirdsView(APIView):
    def get(self, request):
        offset = 0
        if 'offset' in request.query_params and request.query_params['offset'].isnumeric():
            offset = int(request.query_params['offset'])
        limit = -1
        if 'limit' in request.query_params and request.query_params['limit'].isnumeric():
            limit = int(request.query_params['limit'])

        if 'attribute' and 'order' in request.query_params:
            order = '-' if request.query_params['order'] == 'desc' else ''
            if limit > 0:
                serializer = BirdsSerializer(Bird.objects.order_by(order + request.query_params['attribute'])[offset:offset+limit], many=True)
            else:
                serializer = BirdsSerializer(Bird.objects.order_by(order + request.query_params['attribute'])[offset:], many=True)
            return Response(serializer.data)

        if limit > 0:
            serializer = BirdsSerializer(Bird.objects.all()[offset:], many=True)
        else:
            serializer = BirdsSerializer(Bird.objects.all()[offset:offset+limit], many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = BirdsSerializer(data=request.data)
        try:
            if serializer.is_valid():
                new_bird = serializer.validated_data
                if new_bird['body_length'] < 0:
                    return Response('Invalid body length', status=status.HTTP_400_BAD_REQUEST)
                if new_bird['wingspan'] < 0:
                    return Response('Invalid wingspan', status=status.HTTP_400_BAD_REQUEST)
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response(ex.args[0], status=status.HTTP_400_BAD_REQUEST)
