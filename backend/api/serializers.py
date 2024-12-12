"""Comment."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Comment."""

    class Meta:
        """Comment."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
