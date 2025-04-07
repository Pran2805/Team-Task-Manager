from django.shortcuts import render
from rest_framework import viewsets
from tasks.models import task, subtask
from tasks.serializers import taskSerializer ,subtaskSerializer

# Create your views here.
class taskViewSet(viewsets.ModelViewSet):
    queryset = task.objects.all()
    serializer_class = taskSerializer

class subtaskViewSet(viewsets.ModelViewSet):
    queryset = subtask.objects.all()
    serializer_class = subtaskSerializer   