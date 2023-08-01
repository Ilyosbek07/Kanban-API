from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.models import Kanban
from apps.api.serializers import KanbanSerializer


class KanbanListMV(APIView):
    def get(self, request):
        kanban_list = Kanban.objects.all()
        serializer = KanbanSerializer(kanban_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = KanbanSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class KanbanDetailMV(APIView):
    def get(self, request, pk):
        try:
            kanban_detail = Kanban.objects.get(pk=pk)
            serializer = KanbanSerializer(kanban_detail)
        except kanban_detail.DoesNotExist:
            return Response({'error': 'Movie not found', "status": status.HTTP_404_NOT_FOUND})
        return Response(serializer.data)

    def put(self, request):
        serializer = KanbanSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = Kanban.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
