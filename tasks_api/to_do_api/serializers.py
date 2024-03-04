from .models import Task
from rest_framework import serializers


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'due_date', 'name', 'completed']
        extra_kwargs = {'due_date': {"required": False}}
