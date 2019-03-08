from rest_framework import serializers
from todo.models import todoItem

class TodoItemSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.ReadOnlyField()
    class Meta:
        model = todoItem
        fields = ('url', 'title', 'completed', 'order')