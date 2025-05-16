from rest_framework import serializers
from .models import Task
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'description', 'time_sensitive',
                  'time_to_complete','created_at','updated_at']
