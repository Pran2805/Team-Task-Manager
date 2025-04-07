from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from tasks.views import taskViewSet   , subtaskViewSet

routers = routers.DefaultRouter()
routers.register('task', taskViewSet, basename='task')
routers.register('subtask', subtaskViewSet, basename='subtask')
urlpatterns = [

    path('', include(routers.urls)),
]


