from django.forms import ModelForm
from .models import TaskList

class TaskForm(ModelForm):
    class Meta:
        model = TaskList
        fields = [
            'task',
            'completed',
        ]