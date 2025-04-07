from rest_framework import serializers
from tasks.models import task, subtask

class taskSerializer(serializers.HyperlinkedModelSerializer):
    task_id = serializers.ReadOnlyField()
    task_name = serializers.ReadOnlyField()

    class Meta:
        model = task
        fields = "__all__"

class subtaskSerializer(serializers.HyperlinkedModelSerializer):
   task_id = serializers.ReadOnlyField()
   task_name = serializers.ReadOnlyField()
   
   class Meta:
        model = subtask
        fields = "__all__"
